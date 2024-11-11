from tkinter import * 
from tkinter import ttk

root = Tk()

style = ttk.Style()
btn1 = ttk.Button(root, text='Button1')
btn2 = ttk.Button(root, text='Button2')
btn3 = ttk.Button(root, text='Button3')
btn1.pack()
btn2.pack()
btn3.pack()

print(btn1.winfo_class())
print(style.theme_names())
print(style.theme_use())
# style.theme_use('classic')
style.configure('TButton', foreground='black')
style.configure('Alarm.TButton', foreground='green')
style.map('TButton', foreground=[('disabled', 'gray'), ('pressed', 'orange')])
btn3.config(style='Alarm.TButton')

# print (style.layout('TButton'),
#         style.element_options('TButton'),
#         style.lookup('TButton', 'foreground')
# )
root.mainloop()