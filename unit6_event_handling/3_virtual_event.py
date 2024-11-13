from tkinter import * 

# virtual event => mouse event + keyboard event => << >> 
root = Tk()
entry = Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda action:print('copy'))
entry.bind('<<Paste>>', lambda action:print('paste'))

entry.event_add('<<OddNum>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNum>>', lambda action:print('Odd Number'))

# entry.event_generate('<<Paste>>') #invoke the funtion
# entry.delete('<<OddNum>>') # delete the function
# print(entry.event_info('<<OddNum>>'))

root.bind_all('<Escape>', lambda action:print('escape'))

root.mainloop()