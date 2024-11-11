from tkinter import * 
from tkinter import ttk 
from PIL import Image
from PIL import ImageTk

root = Tk() 

treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert('', '0', 'root', text='root')
treeview.insert('root', '0', 'usr', text='usr')
treeview.insert('usr', '0', 'bin', text='bin')
treeview.insert('usr', '1', 'include', text='include')
treeview.insert('usr', '2', 'lib', text='lib')
treeview.insert('usr', '3', 'sbin', text='sbin')

get_img = Image.open('images/ubuntu.ico').resize((15, 15), Image.Resampling.LANCZOS)
ubuntu = ImageTk.PhotoImage(get_img)
treeview.insert('usr', '4', 'ubuntu', text='ubuntu', image=ubuntu)

treeview.insert('', '1', 'home', text='home')
# treeview.detach('bin')
# treeview.move('include', 'home', '0')
# treeview.delete('sbin')

root.mainloop() 