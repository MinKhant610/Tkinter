from tkinter import *
from tkinter import colorchooser

root = Tk()
color = colorchooser.askcolor()
print(color[0])
print(color[1])
root.mainloop()