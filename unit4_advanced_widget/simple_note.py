from tkinter import *
from tkinter import ttk 

class App:
    def __init__(self, master):
        self.master = master 
        self.textArea()
        self.hilightBtn()
        self.hilightRemoveBtn()
        self.selectAllBtn()
    
    def textArea(self):
        self.text_area = Text(self.master, width=30, height=10, wrap=WORD)
        self.text_area.pack()
    
    def hilightBtn(self):
        self.hilight_btn = ttk.Button(self.master, text='Hilight', command=self.applyHilight)
        self.hilight_btn.pack()

    def applyHilight(self):
        self.start = self.text_area.index('sel.first')
        self.end = self.text_area.index('sel.last')
        self.text_area.tag_add('hilight', self.start, self.end)
        self.text_area.tag_configure('hilight', background='yellow')

    def removeHilight(self):
        self.rm_start = self.text_area.index('sel.first')
        self.rm_end = self.text_area.index('sel.last')
        self.text_area.tag_remove('hilight', self.rm_start, self.rm_end)
    
    def hilightRemoveBtn(self):
        self.hilight_remove_btn = ttk.Button(self.master, text='Remove Hilight', command=self.removeHilight)
        self.hilight_remove_btn.pack()
    
    def seletAll(self):
        self.text_area.tag_add('sel', '1.0', 'end')
        self.text_area.mark_set('insert', '1.0')
        self.text_area.see('insert')

    def selectAllBtn(self):
        self.select_all_btn = ttk.Button(self.master, text='Select All', command=self.seletAll)
        self.select_all_btn.pack()



def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()