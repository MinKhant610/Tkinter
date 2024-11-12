from tkinter import * 

# relx = relative x , 0.5 = ratio
root = Tk()
Label(root, text='yellow', background='yellow').place(x=0, y=0)
Label(root, text='light green', background='lightgreen').place(relx=0.5, rely=0.5, anchor=CENTER)
Label(root, text='red', background='red').place(relx=0.5, rely=0.5, x=100, y=50, anchor=CENTER)
root.mainloop()