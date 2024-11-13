from tkinter import * 
from functools import partial

def keyPress(event):
    print(f'type {event.type}')
    print(f'widget {event.widget}')
    print(f'char {event.char}')
    print(f'keysym {event.keysym}')
    print(f'keycode {event.keycode}') 

def shortcut(action):
    print(action)

# with partial function
# def shortcut(action, event):
#     print(action)

root = Tk()

root.bind('<KeyPress>', keyPress)
root.bind('<Command-c>', lambda key:shortcut('Copy'))
# root.bind('<Command-c>', partial(shortcut, 'copy'))
root.mainloop()