import math
import numpy as np
# import tkinter as tk
#
# window = tk.Tk()
# window.geometry("500x800")
# window.resizable(0,0)
# window.title("CALCULATOR")
# window.mainloop()
shift = True

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
    global shift
    if shift:
        shift = False
        return x**(1/3)
    else:
        return math.sqrt(x)

def power(x):
    global shift
    if shift:
        shift = False
        return x**3
    else:
        return x**2

def factorial(x,y):
    global shift
    if shift:
        shift = False
        return x**y
    else:
        return math.factorial(x)

def sine(x) :
    global shift
    if shift:
        shift = False
        return math.asin(x)
    else:
        return math.sin(x)

def cos(x):
    global shift
    if shift:
        shift = False
        return math.acos(x)
    else:
        return math.cos(x)

def tan(x):
    global shift
    if shift:
        shift = False
        return math.atan(x)
    else:
        return math.tan(x)

def log(x,y):
    global shift
    if shift:
        shift = False
        return math.log(x,y)
    else:
        return math.log(x,10)

def constant():
    global shift
    if shift:
        shift = False
        return math.e
    else:
        return math.pi

def qua_equ(a,b,c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        roots = [x1, x2]
        return roots

def cub_equ(a, b, c, d):
    coef = [a, b, c, d]
    return np.roots(coef)

def calc(calculate):
    while True:
        for i in range(len(calculate)):
            if calculate[i] == '(':
                calculate2 = []
                for j in range(i, len(calculate)):
                    if calculate[j] == ')':
                        calculate.insert(0, calc(calculate2))
                        del calculate[i+1:j+2]
                        break
                    calculate2.append(calculate[j])
            if calculate[i] == ')':
                break
            elif calculate[i] == '*':
                calculate.insert(0, multi(calculate[i - 1], calculate[i + 1]))
                del calculate[i:i + 3]
                break
        return calculate[0]


calculate = ['(', 9, '*', 4, ')', '*', 20, '*', '(', 3, '*', 5, ')', '*', 7]
print(calc(calculate))
