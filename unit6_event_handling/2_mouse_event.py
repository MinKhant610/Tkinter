from tkinter import * 
from tkinter import ttk 

def mousePress(event):
    global prev 
    prev = event
    print(f'type {event.type}')
    print(f'widget {event.widget}')
    print(f'num {event.num}') # mouse click 
    print(f'x {event.x}')
    print(f'y {event.y}')

def draw(event):
    global prev 
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
    prev = event

root = Tk()
canvas = Canvas(root, width=600, height=400, bg='white')
canvas.pack()

canvas.bind('<ButtonPress>', mousePress)
canvas.bind('<B1-Motion>', draw)

root.mainloop()