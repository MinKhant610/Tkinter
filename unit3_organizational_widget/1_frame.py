from tkinter import * 
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, width=300, height=400, relief=RIDGE)
frame.pack()
button = Button(frame, text='Click Me')
button.grid()
frame.config(padding=(30, 15))
label_frame = ttk.Labelframe(frame, width=200, height=300, 
                                text='Embedded Linux')
label_frame.grid()
root.mainloop()