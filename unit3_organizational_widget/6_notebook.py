from tkinter import * 
from tkinter import ttk

root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

notebook.add(frame1, text='One')
notebook.add(frame2, text='Two')

frame1_btn = Button(frame1, text='click me')
frame1_btn.pack() 

notebook.insert(1, frame3, text='Three')
# print(notebook.index(notebook.select()))
print(notebook.tab(1, 'text'))
# notebook.tab(2)
notebook.select(1)
notebook.tab(1, state='disabled')

root.mainloop()