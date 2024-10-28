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

