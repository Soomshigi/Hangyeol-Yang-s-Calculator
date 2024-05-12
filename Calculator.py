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

def power(x,y):
    return x ** y
    # global shift
    # if shift:
    #     shift = False
    #     return x**3
    # else:
    #     return x**2

def factorial(x):
    return math.factorial(x)
    # global shift
    # if shift:
    #     shift = False
    #     return x**y
    # else:
    #     return math.factorial(x)

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

def log(x,base):
    return math.log(x, base)
    # global shift
    # if shift:
    #     shift = False
    #     return math.log(x,y)
    # else:
    #     return math.log(x,10)

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
    i = 0
    n = 0
    global shift
    while n < len(calculate):
        while i < len(calculate):
        # for i in range(len(calculate)):
            if calculate[i] == '(':
                calculate2 = []
                for j in range(i+1, len(calculate)):
                    calculate2.append(calculate[j])
                    if calculate[j] == ')':
                        del calculate2[-1]
                        calculate.insert(i, calc(calculate2))
                        del calculate[i+1:j+2]
                        i = 0
                        break
            i += 1
        i = 0
        while i < len(calculate):
            print(calculate)
            print(i)
            if calculate[i] == '√' or calculate[i] == '3√' or calculate[i] == '**' or calculate[i] == 'sin' or calculate[i] == 'cos' or calculate[i] == 'tan' or calculate[i] == 'asin' or calculate[i] == 'acos' or calculate[i] == 'atan' or calculate[i] == 'log' or calculate[i] == '!':
                if calculate[i] == '√':
                    calculate.insert(i, sqrt(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == '3√':
                    shift = True
                    calculate.insert(i, sqrt(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == '**':
                    calculate.insert(i - 1, power(calculate[i - 1],calculate[i + 1]))
                    del calculate[i:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == 'sin':
                    calculate.insert(i, sine(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == 'cos':
                    calculate.insert(i, cos(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == 'tan':
                    calculate.insert(i, tan(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == 'asin':
                    shift = True
                    calculate.insert(i, sine(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == 'acos':
                    shift = True
                    calculate.insert(i, cos(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == 'atan':
                    shift = True
                    calculate.insert(i, tan(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == 'log':
                    calculate.insert(i, log(calculate[i + 2], calculate[i + 1]))
                    del calculate[i+1:i + 4]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == '!':
                    calculate.insert(i, factorial(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
            i += 1
        i = 0
        while i < len(calculate):
            print(calculate)
            print(i)
            # for i in range(len(calculate)):
            if calculate[i] == '/' or calculate[i] == '*':
                if calculate[i] == '/':
                    calculate.insert(i - 1, divide(calculate[i - 1], calculate[i + 1]))
                    del calculate[i:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == '*':
                    calculate.insert(i - 1, multi(calculate[i - 1], calculate[i + 1]))
                    del calculate[i:i + 3]
                    i = 0
                    n = 0
                    continue
            i += 1
        i = 0
        while i < len(calculate):
            print(calculate)
            print(i)
            # for i in range(len(calculate)):
            if calculate[i] == '+' or calculate[i] == '-':
                if calculate[i] == '+':
                    calculate.insert(i - 1, add(calculate[i - 1], calculate[i + 1]))
                    del calculate[i:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == '-':
                    calculate.insert(i - 1, sub(calculate[i - 1], calculate[i + 1]))
                    del calculate[i:i + 3]
                    i = 0
                    n = 0
                    continue
            i += 1
        n += 1
        print("break")
    return calculate[0]
pi = math.pi
e = math.e
calculate = ['3√', 8, '-', '!', 4, '+', 20, '/', 'log', 2, 4, '*', 'acos', -1]
print(calc(calculate))
