from tkinter import * 
from tkinter import ttk

root = Tk()
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progress.config(mode='indeterminate')
progress.pack()
# progress.start()
# progress.stop()
values = DoubleVar()
progress.config(mode='determinate', maximum=11.0, variable=values)
scale = Scale(root, orient=HORIZONTAL, variable=values, from_=0, to=11.0, length=400)
scale.pack()

root.mainloop()