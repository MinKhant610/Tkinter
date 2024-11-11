from tkinter import * 
from tkinter import ttk

root = Tk()

text = Text(root, width=30, height=10, wrap=WORD)
text.grid(row=0, column=0)
scollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
scollbar.grid(row=0, column=1, sticky='NS')
text.config(yscrollcommand=scollbar.set)

root.mainloop()

