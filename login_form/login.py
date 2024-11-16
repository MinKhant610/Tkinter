from tkinter import *
from ttkbootstrap import ttk
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image
from PIL import ImageTk

def login():
    global name_entry, password_entry
    uname = name_entry.get()
    upass = password_entry.get()

    if (uname == '' or upass == ''):
        messagebox.showinfo('Mechtronics', 'Empty Input')
    elif (uname == 'Min Khant' and upass == 'deeplearn'):
        name_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo('Mechtronics', 'Login Success')
        root.destroy()
    else:
        messagebox.showerror('Mechtronics', 'User name and Password not match')
    

root = Tk()
root.title('Mechtronic Login')
root.geometry('500x600')
root.config(bg='white')
root.resizable(False, False)

entry_font = Font(family='Helvetica', size=16)

get_logo = Image.open('images/mclogo.png').resize((270, 270), Image.Resampling.LANCZOS)
mc_logo = ImageTk.PhotoImage(get_logo)

ttk.Label(root, image=mc_logo).grid(row=0, column=0, columnspan=2, padx=5)
title = ttk.Label(root, text='Welcome to Mechtronics Deparment', font=('Helvetica', 24, 'bold'))
title.grid(row=1, column=0, columnspan=2, padx=30)

user_name = ttk.Label(root, text='User Name')
user_name.grid(row=2, column=0, pady=25)
password = ttk.Label(root, text='Password')
password.grid(row=3, column=0, pady=18)

name_entry = ttk.Entry(root, width=20, font=entry_font)
name_entry.grid(row=2, column=1, pady=25, sticky=NW)
password_entry = ttk.Entry(root, width=20, font=entry_font, show='*')
password_entry.grid(row=3, column=1, pady=18, sticky=NW)

login_btn = ttk.Button(root, text='Login', width=19, style='info.TButton', command=login)
login_btn.grid(row=4, column=1, pady=25, sticky=NW)

root.mainloop()