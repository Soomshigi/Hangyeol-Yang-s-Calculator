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
def sqrt(x,shift):
    if shift:
        return math.cbrt(x)
    else:
        return math.sqrt(x)
def power(x,shift):
    if shift:
        return x**3
    else:
        return x**2
def factorial(x,y,shift):
    if shift:
        return x**y
    else:
        return math.factorial(x)
def sine(x,shift):
    if shift:
        return math.asin(x)
    else:
        return math.sin(x)
def cos(x,shift):
    if shift:
        return math.acos(x)
    else:
        return math.cos(x)
def tan(x,shift):
    if shift:
        return math.atan(x)
    else:
        return math.tan(x)
def log(x,y,shift):
    if shift:
        return math.log(x,y)
    else:
        return math.log(x,10)
def constant(shift):
    if shift:
        return math.e
    else:
        return math.pi
shift = False
print(log(100,10,shift))
