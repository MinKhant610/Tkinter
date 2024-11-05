from tkinter import * 
root = Tk() 

button = Button(root, text='click me')
button.pack()
lable = Label(root, text='Python Tkinter')
lable.pack()
button.config(text='press me')
button['text'] = 'hit button'
root.mainloop()