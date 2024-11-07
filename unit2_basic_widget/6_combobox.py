#drop down
from tkinter import * 
from tkinter import ttk

root = Tk()
programming = StringVar()
combobox = ttk.Combobox(root, textvariable=programming)
combobox.pack()
combobox.config(values=('Python', 'C++', 'Javascript', 'PHP'))
combobox.config(state='readonly')
root.mainloop()
