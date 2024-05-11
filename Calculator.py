import math
# import tkinter as tk
#
# window = tk.Tk()
# window.geometry("500x800")
# window.resizable(0,0)
# window.title("CALCULATOR")
# window.mainloop()
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x / y
    else:
        return 'Error! Division by zero is not allowed.'
def sqrt(x):
    return math.sqrt(x)
def square(x):
    return x**2
def power(x,y):
    return x**y
pi = math.pi
