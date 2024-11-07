from tkinter import * 
from tkinter import ttk

root = Tk()

paned_window = ttk.PanedWindow(root, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)

frame1 = ttk.Frame(paned_window, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(paned_window, width=200, height=400, relief=SUNKEN)

frame3 = ttk.Frame(paned_window, width=50, height=100, relief=SUNKEN)

paned_window.add(frame1, weight=1)
paned_window.add(frame2, weight=4)
paned_window.insert(1, frame3)
paned_window.forget(1)
#forget not destory frame3 if we want paned_window.add(frame3)
root.mainloop()