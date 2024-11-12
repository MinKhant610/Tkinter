from tkinter import * 
from tkinter import ttk 
root = Tk() 

#ipadx = internal padding x-axis 
#padx = padding x-axis

Label(root, text='Python', background='yellow').pack(fill=BOTH, expand=True)
Label(root, text='C++', background='skyblue').pack(fill=BOTH, expand=True)
Label(root, text='Javascript', background='lightgreen').pack(fill=BOTH, expand=True)

Label(root, text='Python', bg='yellow').pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
Label(root, text='C++', background='skyblue').pack(side=LEFT, fill=BOTH, expand=True, ipadx=5, ipady=5)
Label(root, text='Javascript', background='lightgreen').pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

for widget in root.pack_slaves():
    widget.pack_configure(padx=5, pady=5)
    # print(widget.pack_info())

root.mainloop()