from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def prompt():
    messagebox.showinfo('Show info', 'welcome!')
    messagebox.showwarning('Show warning', 'Something went wrong!')
    messagebox.showerror('Show error', 'Incorrect Operation!')
    messagebox.askquestion('Ask question', 'Really want to Quit')
    messagebox.askokcancel('as ok cancel', 'Access Location')
    messagebox.askretrycancel('Retry Cancel', 'Incorrect')
    messagebox.askyesno('Yes no', 'Really want to quit')
    messagebox.askyesnocancel('yes no cancle', 'start python?')

root = Tk()
btn = ttk.Button(root, text='message box', command=prompt).pack()
root.mainloop()