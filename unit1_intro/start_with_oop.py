# pack => widget.pack(side=left) 
# grid => two dimision => widget.grid(row=0, column=0)
# place => with pixel => widget.place(x=200, y=100)

# label => event binding 
# button => command call back

from tkinter import * 

class HelloApp:
    def __init__(self, master):
        self.label = Label(master, text='Hello Tkinter')
        self.label.grid(row=0, column=0, columnspan=2)

        Button(master, text='click me', 
        command=self.change_click).grid(row=1, column=1)

        Button(master, text='python', 
        command=self.change_python).grid(row=1, column=2)

    def change_click(self):
        self.label.config(text='You Change the title!')
    
    def change_python(self):
        self.label.config(text='welcom to python tkinter')

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

