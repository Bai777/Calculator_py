from tkinter import messagebox as mb

def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        mb.showerror('Ошибка', 'Делить на ноль нельзя!')
        raise ZeroDivisionError('Деление на ноль')
    return number1 / number2