from tkinter import *
#Intvar, StringVar, DoubleVar, BooleanVar

def show_data():
    label = Label(root, text=python.get())
    label.pack()

root = Tk()
python = StringVar()
py_check_button = Checkbutton(root, text='Python', 
                    variable=python, onvalue='You Choose Python',
                    offvalue='Not choose python', command=show_data)
py_check_button.pack()

root.mainloop()