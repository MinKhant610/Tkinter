from tkinter import * 
from tkinter import ttk 
from PIL import Image
from PIL import ImageTk

def callback(event):
    print(treeview.selection())

root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'item1', text='First')
treeview.insert('item1', '0', 'item2', text='Second')
get_img = Image.open('images/ubuntu.ico').resize((15, 15), Image.Resampling.LANCZOS)
ubuntu = ImageTk.PhotoImage(get_img)
treeview.insert('item2', '0', 'ubuntu', text='ubuntu', image=ubuntu)

treeview.bind('<<TreeviewSelect>>', callback)

treeview.config(columns=('version'))
treeview.column('version', width=50, anchor='center')
treeview.heading('version', text='Version')
treeview.set('ubuntu', 'version', '6.6.32')

root.mainloop()