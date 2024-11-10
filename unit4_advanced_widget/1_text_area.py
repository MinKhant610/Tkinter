from tkinter import * 
from PIL import Image
from PIL import ImageTk

root = Tk()
text = Text(root, width=40, height=10, wrap=WORD)
text.pack()

# text.config(state='disabled')
# line.char => 1.0 => line 1 char 0 
# text.insert('1.0', 'inserted message')
# text.delete('1.0', 'end')
# text.replace('1.0', '1.0 linend', 'this is replace')
# text.get('1.0', 'end')
# text.tag_add('hilight', '1.0', '1.end')
# text.configure('hilight', background='yellow')
# text.tag_delete('hilight')
# insert hello to current cursor location
# text.insert('insert', 'hello')
# move cursor to in front of first line  
# text.mark_set('insert', '1.0')

get_img = Image.open('images/ubuntu.ico')
ubuntu = ImageTk.PhotoImage(get_img)
text.image_create('insert', image=ubuntu)
btn = Button(text, text='click me')
text.window_create('insert', window=btn)

root.mainloop()