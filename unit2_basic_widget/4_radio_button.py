from tkinter import * 

def show_data():
    label = Label(root, text='you choose '+programming.get())
    label.pack()

root = Tk()
programming = StringVar()

Radiobutton(root, text='Python', variable=programming, 
value='python', command=show_data).pack()
Radiobutton(root, text='C++', variable=programming, 
value='C++', command=show_data).pack()
Radiobutton(root, text='Javascript', variable=programming, 
value='Javascript', command=show_data).pack()
Radiobutton(root, text='PHP', variable=programming, 
value='PHP', command=show_data).pack()

root.mainloop()