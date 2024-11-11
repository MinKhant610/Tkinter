from tkinter import * 
from PIL import Image
from PIL import ImageTk

# ⌃  ⌥  ⌘  ⇧  

root = Tk() 

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New File', command=lambda:print('Open New File'))
file_menu.add_command(label='Open', command=lambda:print('Open File'))
file_menu.add_command(label='Save', command=lambda:print('Save File'))
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
menu_bar.add_cascade(label='File', menu=file_menu)


get_img = Image.open('images/command.png')
cmd_img = ImageTk.PhotoImage(get_img)
file_menu.entryconfig('New File', image=cmd_img, compound='left')
file_menu.entryconfig('Open', accelerator='⌘')

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', command=lambda:print('Undo'))
edit_menu.add_command(label='Redo', command=lambda:print('Redo'))
menu_bar.add_cascade(label='Edit', menu=edit_menu)

root.mainloop() 
