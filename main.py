from tkinter import *
from tkinter import ttk
import calculator_logic as calc

operation = ''
first = 0
second = 0
result = 0


def calculation():
    second = float(entry.get())
    if operation == '+':
        result = calc.add(first, second)
    elif operation == '-':
        result = calc.subtract(first, second)
    elif operation == '*':
        result = calc.multiply(first, second)
    elif operation == '/':
        result = calc.divide(first, second)
    entry.delete(0, END)
    entry.insert(0, str(result))


def input_number(number):
    entry.insert(END, number)


def clear_entry():
    entry.delete(0, END)


def set_operation(set_oper):
    global first
    global operation
    first = float(entry.get())
    operation = set_oper
    entry.delete(0, END)


def validate_entry():
    entry_window = entry.get()
    text_entry = ''.join(b for b in entry_window if b in '0123456789.-')
    if entry_window != text_entry:
        entry.delete(0, END)
        entry.insert(0, text_entry)


window = Tk()
window.title('Калькулятор')

entry = ttk.Entry()
entry.grid(row=0, column=0, columnspan=4, sticky='ew')
entry.bind('<KeyRelease>', lambda event: validate_entry())

ttk.Button(text='1', command=lambda: input_number('1')).grid(row=1, column =0)
ttk.Button(text='2', command=lambda: input_number('2')).grid(row=1, column =1)
ttk.Button(text='3', command=lambda: input_number('3')).grid(row=1, column =2)
ttk.Button(text='4', command=lambda: input_number('4')).grid(row=2, column =0)
ttk.Button(text='5', command=lambda: input_number('5')).grid(row=2, column =1)
ttk.Button(text='6', command=lambda: input_number('6')).grid(row=2, column =2)
ttk.Button(text='7', command=lambda: input_number('7')).grid(row=3, column =0)
ttk.Button(text='8', command=lambda: input_number('8')).grid(row=3, column =1)
ttk.Button(text='9', command=lambda: input_number('9')).grid(row=3, column =2)
ttk.Button(text='0', command=lambda: input_number('0')).grid(row=4, column =0)

ttk.Button(text='C', command=clear_entry).grid(row=4, column =1)
ttk.Button(text='=', command=calculation).grid(row=4, column =2)

ttk.Button(text='+', command=lambda: set_operation('+')).grid(row=1, column =3)
ttk.Button(text='-', command=lambda: set_operation('-')).grid(row=2, column =3)
ttk.Button(text='*', command=lambda: set_operation('*')).grid(row=3, column =3)
ttk.Button(text='/', command=lambda: set_operation('/')).grid(row=4, column =3)

window.mainloop()