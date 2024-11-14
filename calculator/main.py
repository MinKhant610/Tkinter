from tkinter import *
from tkinter import ttk

def btnClick(numbers):
    global operator
    operator += numbers
    text_input.set(operator)

cal = Tk()
cal.title('Calculator')
operator = ''
text_input = StringVar()

cal.resizable(FALSE, FALSE)
style = ttk.Style()
style.theme_use('default')
style.configure('TButton', background='powder blue', 
                foreground='black', font=('Helvetica', 20, 'bold'), 
                padx=16, pady=16, borderwidth=8, width=4)

text_display = Entry(cal, font=('Helvetica', 20, 'bold'),
                    bg='powder blue', textvariable=text_input, bd=30, 
                    insertwidth=4, justify=RIGHT)
text_display.grid(row=0, column=0, columnspan=4)
text_display.config(state='readonly')

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

# Create buttons in a loop with the correct lambda scope
for text, row, col in buttons:
    if text.isdigit() or text in ['+', '-', '*', '/']:
        command = lambda t=text: btnClick(t)  # Capture `text` as `t` in each lambda
    elif text == 'C':
        command = lambda: btn_clear() 
    elif text == '=':
        command = lambda: evaluate()  
    else:
        command = None
    ttk.Button(cal, text=text, width=5, command=command).grid(row=row, column=col)

def evaluate():
    global operator
    try:
        result = str(eval(operator))
        text_input.set(result)
        operator = result 
    except:
        text_input.set("Error")
        operator = ""

def btn_clear():
    global operator
    operator = ''
    text_input.set('')

cal.mainloop()
