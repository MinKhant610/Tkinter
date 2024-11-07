from tkinter import * 
from PIL import Image
from PIL import ImageTk

root = Tk() 
label = Label(root, text='Ubuntu Linux', 
            font=('Helvetica', 18, 'bold'))
label.pack()
label.config(foreground='#dd4814', background='white')
label.config(wraplength=150, justify=CENTER)

get_logo = Image.open('images/ubuntu.png')
logo_img = ImageTk.PhotoImage(get_logo)
label.config(image=logo_img, compound='left')

root.mainloop()