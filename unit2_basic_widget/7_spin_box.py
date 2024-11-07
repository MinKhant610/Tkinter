from tkinter import *

root = Tk()
years = StringVar()
spinbox = Spinbox(root, textvariable=years)
spinbox.pack()
spinbox.config(from_=1900, to=2024, increment=2)
spinbox.config(state='readonly')

root.mainloop()