from tkinter import * 

root = Tk() 

entry = Entry(root, width=30)
entry.pack()
# entry.config(state='disabled')
entry.insert(0, 'Hello Tkinter')
# entry.config(state='readonly')
entry.delete(0, 1)
# entry.get()
root.mainloop()
