from tkinter import * 
from functools import partial

def changeState(name):
    top_window.state(name)

def changeLevel(name, window):
    #top_window.lower(root)
    method = getattr(top_window, name, None)
    if callable(method):
        method(window)

def minMax(name):
    #top_window.iconify()
    method = getattr(top_window, name, None)
    if callable(method):
        method()

root = Tk()
root.geometry('600x600')
root.title('Root window')
label = Label(root, text='hello root')
label.pack()

top_window = Toplevel()
top_window.geometry('300x300')
top_window.title('Top window')

iconify_btn = Button(root, text='iconify', 
                        command=partial(minMax, 'iconify'))
iconify_btn.pack()
deiconify_btn = Button(root, text='deiconify', 
                        command=partial(minMax, 'deiconify'))
deiconify_btn.pack()
normal = Button(root, text='normal', 
                        command=partial(changeState, 'normal'))
normal.pack()
zoomed = Button(root, text='zoomed', 
                        command=partial(changeState, 'zoomed'))
zoomed.pack()
withdrawn = Button(root, text='withdrawn', 
                        command=partial(changeState, 'withdrawn'))
withdrawn.pack()
lower = Button(top_window, text='lower', 
                    command=partial(changeLevel, 'lower', root))
lower.pack()
lift = Button(root, text='lift', 
                        command=partial(changeLevel, 'lift', root))
lift.pack()

root.maxsize(600, 600)
root.minsize(300, 300)
# root.resizable(False, False)
root.mainloop()