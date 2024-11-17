import tkinter as tk 
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from PIL import Image
from PIL import ImageTk
import pymysql
import os 
import shutil
import db_config

def onTabSelected(event):
    global blank_textboxes_tab_two, image_selected
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, 'text')

    if tab_text == 'All Records':
        if (blank_textboxes_tab_two == False and image_selected == True):
            load_database_results()
    
    if tab_text == 'Add New Record':
        blank_textboxes_tab_two = True
        image_selected = False

def load_database_results():
    global rows, num_of_rows
    try:
        connection = pymysql.connect(
            host=db_config.db_server,
            user=db_config.db_user,
            password=db_config.db_pass,
            database=db_config.db_name
            )

        sql = 'select * from tbl_employees'   
        cursor = connection.cursor() 
        cursor.execute(sql)
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount
        cursor.close()

        connection.close()
        has_loaded_successfully = True

    except pymysql.InterfaceError as error:
        has_loaded_successfully = databaseError(error)

    except pymysql.OperationalError as error:
        has_loaded_successfully = databaseError(error)
    
    except pymysql.ProgrammingError as error:
        has_loaded_successfully = databaseError(error)

    except pymysql.DataError as error:
        has_loaded_successfully = databaseError(error)    
    
    except pymysql.IntegrityError as error:
        has_loaded_successfully = databaseError(error)
    
    except pymysql.NotSupportedError as error:
        has_loaded_successfully = databaseError(error)
    
    return has_loaded_successfully

def databaseError(error):
    Messagebox.show_error(title='Database status', message=error, alert=True)
    return False

def imagePath(file_path):
    open_image = Image.open(file_path).resize((120, 120), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(open_image)

    return image

def load_img_tab1(file_path):
    image = imagePath(file_path)
    imagelabel_tab1.configure(image=image)
    imagelabel_tab1.image = image 

def scroll_forward():
    global row_counter, num_of_rows

    if row_counter >= num_of_rows-1:
        Messagebox.show_info(title='DB Status', message='End of file', alert=True)
    else:
        row_counter+=1
        scroll_load()

def scroll_backward():
    global row_counter, rows
    if row_counter == 0:
        Messagebox.show_info(title='DB Status', message='No backward file', alert=True)
    else:
        row_counter-=1
        scroll_load()

def scroll_load():
    fName.set(rows[row_counter][1])
    lName.set(rows[row_counter][2])
    job.set(rows[row_counter][3])
    try:
        img_path = db_config.photo_directory + rows[row_counter][4]
        load_img_tab1(img_path)
    except FileNotFoundError as err:
        load_img_tab1(db_config.photo_directory+'default.png')

def load_img_tab2(file_path):
    image = imagePath(file_path)
    imagelabel_tab2.configure(image=image)
    imagelabel_tab2.image = image

def select_image():
    global image_selected, image_file_name
    global file_to_copy, file_new_home

    path_to_image = filedialog.askopenfilename(
        initialdir='/',
        title='Open File',
        filetypes=(
            ('PNGs',"*.png" ), 
            ('GIFs', '*gif'),
            ('JPGs', '*.jpg'),
            ('All Files', '*.*')
        )
    )
    try:
        if path_to_image:
            image_file_name = os.path.basename(path_to_image)
            file_new_home = db_config.photo_directory + image_file_name
            file_to_copy = path_to_image
            image_selected = True
            load_img_tab2(file_to_copy)
    except IOError as error:
        image_selected = False
        Messagebox.show_error(title='IO Status', message=error, alert=True)

def insert_to_db(first, last, job_field, photo):
    try:
        connection = pymysql.connect(
            host=db_config.db_server,
            user=db_config.db_user,
            password=db_config.db_pass,
            database=db_config.db_name
        )

        # Fix the SQL syntax
        sql = 'INSERT INTO tbl_employees (First_Name, Last_Name, Job_Title, Photo) VALUES (%s, %s, %s, %s)'

        # Create tuple of values
        vals = (first, last, job_field, photo)

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(sql, vals)
        connection.commit()
        cursor.close()
        connection.close()

        # Show success message
        Messagebox.show_info(title='DB Status', message='Record Added Successfully', alert=True)
        first_entry_tab2.delete(0, 'end')
        last_entry_tab2.delete(0, 'end')
        job_entry_tab2.delete(0, 'end')
        load_img_tab2(db_config.photo_directory+'default.png')

    except (pymysql.InterfaceError, pymysql.OperationalError, pymysql.ProgrammingError,
            pymysql.DataError, pymysql.IntegrityError, pymysql.NotSupportedError) as error:
        databaseError(error)

def add_new_record():
    global blank_textboxes_tab_two
    global file_new_home, file_to_copy

    blank_textboxes_count = 0 
    if fName_tab2.get == '':
        blank_textboxes_count+=1
    if lName_tab2.get == '':
        blank_textboxes_count+=1
    if job_tab2.get == '':
        blank_textboxes_count+=1
    
    if blank_textboxes_count > 0:
        blank_textboxes_tab_two = True
        Messagebox.show_error(title='DB Status', message='Empyt entry', alert=True)
    else:
        blank_textboxes_tab_two = False

        if image_selected:
            try:
                shutil.copy(file_to_copy, file_new_home)
            except shutil.SameFileError as error:
                Messagebox.show_error(title='DB Status', message=error, alert=True)

            insert_to_db(fName_tab2.get(), lName_tab2.get(), job_tab2.get(), image_file_name) 
        else:
            Messagebox.show_info(title='DB Status', message='please select photo', alert=True)


file_name = 'default.png'
path = db_config.photo_directory + file_name
rows = None
num_of_rows = None 
row_counter = 0

image_selected = False
image_file_name = None 
file_to_copy = None 
file_new_home = None 
blank_textboxes_tab_two = True

form = ttk.Window(themename='litera')
form.title('MC Employees Database form')
form.geometry('500x280')

tab_parent = ttk.Notebook(form, bootstyle='primary')

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>", onTabSelected)

tab_parent.add(tab1, text='All Records')
tab_parent.add(tab2, text='Add New Record')

#setup string variable for database
fName = ttk.StringVar()
lName = ttk.StringVar()
job = ttk.StringVar()

fName_tab2 = ttk.StringVar()
lName_tab2 = ttk.StringVar()
job_tab2 = ttk.StringVar()

# for tab1
first_name = ttk.Label(tab1, text='First Name')
last_name = ttk.Label(tab1, text='Last Name')
job_title = ttk.Label(tab1, text='Job Title')

# get_img_tab1 = Image.open(path).resize((120, 120), Image.Resampling.LANCZOS)
image_tab1 = imagePath(path)
imagelabel_tab1 = ttk.Label(tab1, image=image_tab1)

first_entry = ttk.Entry(tab1, textvariable=fName)
last_entry = ttk.Entry(tab1, textvariable=lName)
job_entry = ttk.Entry(tab1, textvariable=job)

back_btn = ttk.Button(tab1, text='Back', bootstyle='success', command=scroll_backward)
forward_btn = ttk.Button(tab1, text='Forward', bootstyle='success', command=scroll_forward)

#widget placement
first_name.grid(row=0, column=0, padx=15, pady=15)
last_name.grid(row=1, column=0, padx=15, pady=15)
job_title.grid(row=2, column=0, padx=15, pady=15)
imagelabel_tab1.grid(row=0, column=2, rowspan=3, padx=15, pady=15)

first_entry.grid(row=0, column=1, padx=15, pady=15)
last_entry.grid(row=1, column=1, padx=15, pady=15)
job_entry.grid(row=2, column=1, padx=15, pady=15)

back_btn.grid(row=3, column=0, padx=15, pady=15)
forward_btn.grid(row=3, column=2, padx=15, pady=15)

#for tab2 
first_name = ttk.Label(tab2, text='First Name')
last_name = ttk.Label(tab2, text='Last Name')
job_title = ttk.Label(tab2, text='Job Title')

# get_img_tab2 = Image.open(path).resize((120, 120), Image.Resampling.LANCZOS)
image_tab2 = imagePath(path)
imagelabel_tab2 = ttk.Label(tab2, image=image_tab2)

first_entry_tab2 = ttk.Entry(tab2, textvariable=fName_tab2)
last_entry_tab2 = ttk.Entry(tab2, textvariable=lName_tab2)
job_entry_tab2 = ttk.Entry(tab2, textvariable=job_tab2)

add_record_btn = ttk.Button(tab2, text='Add Record to Database', bootstyle='success', command=add_new_record)
add_image_btn = ttk.Button(tab2, text='Add Image', bootstyle='success', command=select_image)

#widget placement
first_name.grid(row=0, column=0, padx=15, pady=15)
last_name.grid(row=1, column=0, padx=15, pady=15)
job_title.grid(row=2, column=0, padx=15, pady=15)
imagelabel_tab2.grid(row=0, column=2, rowspan=3, padx=15, pady=15)

first_entry_tab2.grid(row=0, column=1, padx=15, pady=15)
last_entry_tab2.grid(row=1, column=1, padx=15, pady=15)
job_entry_tab2.grid(row=2, column=1, padx=15, pady=15)

add_record_btn.grid(row=3, column=1, padx=15, pady=15)
add_image_btn.grid(row=3, column=2, padx=15, pady=15)

tab_parent.pack(expand=True, fill='both')
success = load_database_results()

if success:
    fName.set(rows[0][1])
    lName.set(rows[0][2])
    job.set(rows[0][3])
    photo_path = db_config.photo_directory + rows[0][4]
    load_img_tab1(photo_path)

form.mainloop()

