from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from tkinter.font import Font
import sqlite3


#database 
connection = sqlite3.connect('userdata.db')
cursor = connection.cursor()
cursor.execute(
    '''create table if not exists record(
    name text,
    email text,
    contact number,
    gender text,
    country text,
    password text
    )'''
)
connection.commit()

def validate_field(value, field_name):
    if not value:
        return f"{field_name} can't be empty"
    return None

#data insert to database
def insertData():
    try:
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()
        cursor.execute(""" insert into record values (
        :name, :email, :contact, :gender, :country, :password) """, {
            'name':register_name.get(),
            'email':register_email.get(),
            'contact':register_mobile.get(),
            'gender':gender.get(),
            'country':variable.get(),
            'password':register_password.get()
        })
        connection.commit()
        Messagebox.show_info(title='', message='Record Successfully', alert=TRUE)

        register_name.delete(0, END)
        register_email.delete(0, END)
        register_mobile.delete(0, END)
        register_password.delete(0, END)
        re_enter_pass.delete(0, END)

    except Exception as error:
        Messagebox.show_error(title='', message=error, alert=True) 


def insert():
    warn = None

    # Validate all fields
    fields = [
        (register_name.get(), "Name"),
        (register_email.get(), "Email"),
        (register_password.get(), "Password"),
        (re_enter_pass.get(), "Re-enter password"),
        (register_mobile.get(), "Contact"),
        (gender.get(), "Gender"),
        (variable.get(), "Country"),
    ]

    for value, field_name in fields:
        warn = validate_field(value, field_name)
        if warn:
            break

    # Additional validation for password match
    if not warn and register_password.get() != re_enter_pass.get():
        warn = "Passwords didn't match!"

    # Output or use `warn` as needed
    if warn:
        Messagebox.show_error(title='', message=warn, alert=True)
    else:
        insertData()

def login_response(usr_mail, usr_pass):
    if (user_email.get() == usr_mail and user_password.get() == usr_pass):
            Messagebox.show_info(title='Login Status', message='Login Success', alert=True)
            user_email.delete(0, END)
            user_password.delete(0, END)
    else:
        Messagebox.show_error(title='Login Status', message='email and password not match', alert=True)


def login():
    warn = None
    try:
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        for row in cursor.execute('select * from record'):
            usr_mail = row[1]
            usr_pass = row[5] 
    except Exception as error:
        Messagebox.show_error(title='', message=error, alert=True)
    
    fields = [
        (user_email.get(), 'Email',),
        (user_password.get(), 'Password')
    ]

    for value, field in fields:
        warn = validate_field(value, field)
        if warn:
            break 

    if warn:
        Messagebox.show_error(title='', message=warn, alert=True)
    else:
        login_response(usr_mail, usr_pass)
            


ws = ttk.Window(themename="litera")
ws.title('Mechtronics Login')
ws.geometry('940x540')
ws.config(bg='#0B5A81')
ws.resizable(False, False)

font_ = Font(family='Helvetica', size=14)

right_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10,
)

# Label placement
labels = [
    ('Name', 0, 0),
    ('Email', 1, 0),
    ('Password', 2, 0),
    ('Re-Enter Password', 3, 0),
    ('Contact Number', 4, 0),
    ('Gender', 5, 0),
    ('Select Country', 6, 0)
]

for text, row, column in labels:
    ttk.Label(
        right_frame,
        text=text,
        font=font_,
        bootstyle='dark'
    ).grid(row=row, column=column, sticky=W, pady=10)

#Entry field
register_name = ttk.Entry(
    right_frame,
    font=font_,
    width=27
)

register_email = ttk.Entry(
    right_frame,
    font=font_,
    width=27
)
register_password = ttk.Entry(
    right_frame,
    font=font_,
    width=27,
    show='*'
)
re_enter_pass = ttk.Entry(
    right_frame,
    font=font_,
    width=27,
    show='*'
)
register_mobile = ttk.Entry(
    right_frame,
    font=font_,
    width=27
)

#gender frame
gender_frame = ttk.LabelFrame(
    right_frame,
    text='Select Gender',
    bootstyle='dark',
)

gender = StringVar()
gender.set('male')

male_radio_btn = ttk.Radiobutton(
    gender_frame,
    text='Male',
    bootstyle='info',
    padding=10,
    value='male',
)

female_radio_btn = ttk.Radiobutton(
    gender_frame,
    text='Female',
    bootstyle='info',
    padding=10,
    value='female'
)

others_radio_btn = ttk.Radiobutton(
    gender_frame,
    text='others',
    bootstyle='info',
    padding=10,
    value='others'
)

#countries
countries = []
variable = StringVar()
world = open('/Users/minkhant/tkinter/login_form/countries.txt')

for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[12])

register_country = ttk.OptionMenu(
    right_frame,
    variable,
    countries[12],
    *countries,
    bootstyle='dark'
)

register_btn = ttk.Button(
    right_frame,
    width=20,
    text='Register',
    cursor='hand2',
    padding=5,
    bootstyle='success',
    command=insert
)

#right frame widget placement
register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20)
register_password.grid(row=2, column=1, pady=10, padx=20)
re_enter_pass.grid(row=3, column=1, pady=10, padx=20)
register_mobile.grid(row=4, column=1, pady=10, padx=20)
register_country.grid(row=6, column=1, pady=10, padx=20)

gender_frame.grid(row=5, column=1, pady=10, padx=20)
male_radio_btn.pack(side=LEFT, expand=True)
female_radio_btn.pack(side=LEFT, expand=True)
others_radio_btn.pack(side=LEFT, expand=True)

#btn placement
register_btn.grid(row=7, column=0, columnspan=2, pady=15, ipady=3)

right_frame.place(x=470, y=40)

left_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10,
)

left_labels = [
    ('Email', 0, 0),
    ('Password', 1, 0),
]

for text, row, column in left_labels:
    ttk.Label(
        left_frame,
        text=text,
        font=font_,
        bootstyle='dark'
    ).grid(row=row, column=column, sticky=W, pady=10)

user_email = ttk.Entry(
    left_frame,
    font=font_,
    width=27
)

user_password = ttk.Entry(
    left_frame,
    font=font_,
    width=27,
    show='*'
)

login_btn = ttk.Button(
    left_frame,
    width=8,
    cursor='hand2',
    padding=5,
    text='Login',
    bootstyle='success',
    command=login
)

#left frame widget placement
user_email.grid(row=0, column=1, pady=10, padx=20)
user_password.grid(row=1, column=1, pady=10, padx=20)

# left_frame button placement
login_btn.grid(row=2, column=0, pady=15, ipady=5)

left_frame.place(x=40, y=40)
ws.mainloop()