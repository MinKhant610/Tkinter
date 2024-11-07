from tkinter import *


def topLevel1():
    top_window1 = Toplevel()
    top_window1.title('Top Level 1')
    top_window1.geometry('300x300')
    top_win2_btn = Button(top_window1, text='Open Top Level 2', 
                    command=topLevel2)
    exit_btn = Button(top_window1, text='Exit', 
                        command=top_window1.destroy)
    top_win2_btn.pack()
    exit_btn.pack()
    top_window1.mainloop()

def topLevel2():
    top_window2 = Toplevel()
    top_window2.title('Top Level 2')
    top_window2.geometry('300x300')
    exit_btn = Button(top_window2, text='Exit', 
                        command=top_window2.destroy)
    exit_btn.pack()
    top_window2.mainloop()

root = Tk()
root.title('Root window')
root.geometry('400x400')

top_win1 = Button(root, text='Open Top Level 1', command=topLevel1)
top_win1.pack()


root.mainloop()