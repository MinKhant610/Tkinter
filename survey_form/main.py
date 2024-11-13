from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

#entry button frame shoud be seperate function not only in init

class Feedback:
    def __init__(self, master):
        self.master = master 
        self.master.title('Mechtronics Survey')
        self.master.resizable(False, False)
        self.master.configure(background='white')

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('TFrame', background='white')
        self.style.configure('TButton', background='white')
        self.style.configure('TLabel', background='white', font=('Helvetica', 14, 'bold'))
        self.style.configure('Header.TLabel', font=('Helvetica', 18, 'bold'))

        #header frame
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        #image
        self.get_logo =  Image.open('images/mclogo.png').resize((110, 110), Image.Resampling.LANCZOS)
        self.mc_logo = ImageTk.PhotoImage(self.get_logo)
        self.logo = ttk.Label(self.frame_header, image=self.mc_logo)
        self.logo.grid(row=0, column=0, rowspan=2)
        #header
        self.header = ttk.Label(self.frame_header, text='Thank for Exploring!', style='Header.TLabel')
        self.header.grid(row=0, column=1)
        self.sub_title = ttk.Label(self.frame_header, text='Welcome to Mechtronics Deparment', wraplength=300)
        self.sub_title.grid(row=1, column=1)

        #content frame 
        self.frame_content = ttk.Frame(self.master)
        self.frame_content.pack()
        self.name = ttk.Label(self.frame_content, text='Name')
        self.name.grid(row=0, column=0, sticky=SW, padx=5, pady=5)
        self.email = ttk.Label(self.frame_content, text='Email')
        self.email.grid(row=0, column=1, sticky=SW, padx=5, pady=5)
        self.comments = ttk.Label(self.frame_content, text='Comments:')
        self.comments.grid(row=2, column=0, sticky=SW, padx=5, pady=5)


        #entry
        self.entry_name = ttk.Entry(self.frame_content, width=26, font=('Helvetica', 14))
        self.entry_name.grid(row=1, column=0, sticky=SW, padx=5, pady=5)
        self.entry_email = ttk.Entry(self.frame_content, width=26, font=('Helvetica', 14))
        self.entry_email.grid(row=1, column=1, sticky=SW, padx=5, pady=5)

        self.text_comments = Text(self.frame_content, width=55, height=10, wrap=WORD, font=('Helvetica', 14))
        self.text_comments.grid(row=3, column=0, columnspan=2, sticky=SW, padx=5, pady=5)

        #button
        self.submit_btn = ttk.Button(self.frame_content, text='Submit', command=self.sumbit)
        self.submit_btn.grid(row=4, column=0, sticky=E, padx=5, pady=10)
        self.clear_btn = ttk.Button(self.frame_content, text='Clear', command=self.clear)
        self.clear_btn.grid(row=4, column=1, sticky=W, padx=5, pady=10)

        for widget in self.master.pack_slaves():
            widget.pack_configure(padx=10)
        
    def sumbit(self):
        print(f'Name : {self.entry_name.get()}') 
        print(f'Email : {self.entry_email.get()}') 
        print(f'Comments : {self.text_comments.get(1.0, END)}')
        self.clear()
        messagebox.showinfo('Mechtronics Survey', 'Submit Successfully')


    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

    
def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop() 

if __name__ == '__main__':
    main()