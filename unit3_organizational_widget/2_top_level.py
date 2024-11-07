from tkinter import *

root = Tk()

root.geometry('500x500')
root.title('Root Window')
root_label = Label(root, text='This is root window')
root_label.pack()

top_window = Toplevel()
top_window.geometry('300x300')
top_window.title('Top Window')
top_label = Label(top_window, text='This is top level window')
top_label.pack()

root.mainloop()