from tkinter import * 

root = Tk()
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.columnconfigure(8, weight=2)
Label(root, text='yellow', bg='yellow').grid(row=0, column=0, sticky=NSEW)
Label(root, text='light green', bg='lightgreen').grid(row=0, column=1, columnspan=6, sticky=NSEW)
Label(root, text='red', bg='red').grid(row=0, column=8, sticky=NSEW, columnspan=2, padx=5)
Label(root, text='skyblue', bg='skyblue').grid(row=1, column=0, sticky=NSEW)
Label(root, text='pink', bg='pink').grid(row=1, column=1, sticky=NSEW)
root.mainloop()