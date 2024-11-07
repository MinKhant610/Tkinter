from tkinter import *
from PIL import Image
from PIL import ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.label_setup()
        self.button_setup()

    def label_setup(self):
        self.label = Label(self.master, text='Hello Tkinter',
                            font=('Helvetica', 18, 'bold'))
        self.label.pack()

    def button_setup(self):
        try:
            self.get_ubuntu = Image.open('images/ubuntu.png').resize((10, 10), Image.Resampling.LANCZOS)
            self.ubuntu_img = ImageTk.PhotoImage(self.get_ubuntu)
            self.button = Button(self.master, text='Linux', font=('Helvetica', 18, 'bold'),
                                image=self.ubuntu_img, command=self.click_linux, compound='left')
            self.button.pack()
            # self.button.config(state='disabled')
            # print(self.button.cget('state'))
            # self.button.invoke()
        except FileNotFoundError:
            self.label.config(text='Image not found')

    def click_linux(self):
        self.label.config(text='You Click Ubuntu Button')

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()