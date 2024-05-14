import tkinter as tk
from tkinter import font
import re
import math
import numpy as np

window = tk.Tk()
window.title("Calculator")

value = ''
value1 = ''
s = False
shift = False
eq = False
eqt = ''
pi = math.pi
e = math.e

my_font = font.Font(family='Helvetica', size=12, weight='bold')
label = tk.Label(window, text=value, font=my_font)
label1 = tk.Label(window, text=value1, font=my_font)
label.grid(row=0,column=0, columnspan=3,)
label1.grid(row=11,column=0, columnspan=3,)

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

def factorial(x):
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

def log(x,base):
    return math.log(x, base)

def constant():
    global shift
    if shift:
        shift = False
        return math.e
    else:
        return math.pi

def qua_equ(a,b,c):
    roots = []
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return roots
    elif d == 0:
        x = -b / (2 * a)
        roots = [x]
        return roots
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        roots = [x1, x2]
        return roots

def cub_equ(a, b, c, d):
    coef = [a, b, c, d]
    roots = np.roots(coef)
    return roots

def calc(calculate):
    i = 0
    n = 0
    global shift
    while n < len(calculate):
        while i < len(calculate):
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
            if calculate[i] == '-' and (i == 0 or calculate[i-1] in ['(', '*', '+', '-', '/']):
                # Combine '-' with the following number to form a negative number
                if i + 1 < len(calculate) and isinstance(calculate[i + 1], (int, float)):
                    calculate[i] = -calculate[i + 1]
                    del calculate[i + 1]
                    i = 0
                    n = 0
                    continue

            if calculate[i] == '√' or calculate[i] == '∛' or calculate[i] == '**' or calculate[i] == 'sin' or calculate[i] == 'cos' or calculate[i] == 'tan' or calculate[i] == 'asin' or calculate[i] == 'acos' or calculate[i] == 'atan' or calculate[i] == 'log' or calculate[i] == '!':
                if calculate[i] == '√':
                    calculate.insert(i, sqrt(calculate[i + 1]))
                    del calculate[i+1:i + 3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == '∛':
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
                elif calculate[i] == 'log10':
                    calculate.insert(i, log(calculate[i + 1], 10))
                    del calculate[i+1:i+3]
                    i = 0
                    n = 0
                    continue
                elif calculate[i] == '!':
                    calculate.insert(i-1, factorial(calculate[i - 1]))
                    del calculate[i:i + 2]
                    i = 0
                    n = 0
                    continue
            i += 1
        i = 0
        while i < len(calculate):
            print(calculate)
            print(i)
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

def button_calculate():
    global value,pi,e,eq,eqt
    calculation = re.split(r'(\b\w*\d*\b|\(|\)|\+|-|\*|/)',value)
    calculation = [i for i in calculation if i.strip()]
    calculation = [int(i) if i.isdigit() else i for i in calculation]
    for i in range(len(calculation)):
        if calculation[i] == '^':
            calculation.insert(i,'**')
            del calculation[i+1]
        elif calculation[i] == 'e':
            calculation.insert(i, e)
            del calculation[i + 1]
        elif calculation[i] == '÷':
            calculation.insert(i, '/')
            del calculation[i + 1]
        elif calculation[i] == 'π':
            calculation.insert(i, pi)
            del calculation[i + 1]
        elif calculation[i] == '×':
            calculation.insert(i, '*')
            del calculation[i + 1]
    if eq and eqt == 'Q':
        print(calculation)
        i = 0
        while i < len(calculation):
            if calculation[i] == '-' and (i == 0 or calculation[i - 1] in ['(', '*', '+', '-', '/']):
                # Combine '-' with the following number to form a negative number
                if i + 1 < len(calculation) and isinstance(calculation[i + 1], (int, float)):
                    calculation[i] = -calculation[i + 1]
                    del calculation[i + 1]
                    i = 0
                    continue
            i += 1
        calculation.remove('(')
        calculation.remove(')')
        calculation.remove('(')
        calculation.remove(')')
        calculation.remove('(')
        calculation.remove(')')
        print(calculation)
        lst = qua_equ(calculation[0],calculation[1],calculation[2])
        value = "Zeros: "
        print(lst)
        for i in range(len(lst)):
            if not isinstance(lst[i], complex):
                value += f"[{str(round(lst[i], 3))}] "
            print(value)
        if len(lst)==0:
            value += "Complex/None "
        label.config(text=value)
        value = ''
        eqt = ''
    elif eq and eqt == 'C':
        i = 0
        while i < len(calculation):
            if calculation[i] == '-' and (i == 0 or calculation[i - 1] in ['(', '*', '+', '-', '/']):
                # Combine '-' with the following number to form a negative number
                if i + 1 < len(calculation) and isinstance(calculation[i + 1], (int, float)):
                    calculation[i] = -calculation[i + 1]
                    del calculation[i + 1]
                    i = 0
                    continue
            i += 1
        calculation.remove('(')
        calculation.remove(')')
        calculation.remove('(')
        calculation.remove(')')
        calculation.remove('(')
        calculation.remove(')')
        calculation.remove('(')
        calculation.remove(')')
        lst = cub_equ(calculation[0], calculation[1], calculation[2], calculation[3])
        value = "Zeros: "
        for i in range(len(lst)):
            print(lst[i])
        print(lst)
        for i in range(len(lst)):
            if np.isclose(lst[i].imag,0):
                value += f"[{str(round(lst[i].real,3))}] "
            print(value)
        label.config(text=value)
        value = ''
    elif not eq:
        value = str(round(calc(calculation), 5))
        label.config(text=value)
        value = ''

def eqnb():
    global eq
    eq = not eq
    if eq:
        label1.config(text='1. ax²+bx+c=0\n2. ax³+bx²+cx+d=0')
    else:
        label1.config(text='')

def button_click(n):
    global value,eq,eqt
    if n == 'Q':
        eqt = 'Q'
        value = ''
    elif n == 'C':
        eqt = 'C'
        value = ''
    else:
        value += n
    if eq and n == 'Q':
        label1.config(text='a:(_) b:(_) c:(_)')
        value = ''
    elif eq and n == 'C':
        label1.config(text='a:(_) b:(_) c:(_) d:(_)')
        value = ''

    if n == 'clear':
        value = ''
    label.config(text=value)
    print(value)

def shiftb():
    global s
    s = not s
    if s:
        button_pi.config(text="e", command=lambda: button_click('e'), padx=40, pady=20)
        button_fact.config( text="^y", command=lambda: button_click('^('), padx=40, pady=20)
        button_sin.config( text="sin⁻¹", command=lambda: button_click('asin('), padx=40, pady=20)
        button_cos.config( text="cos⁻¹", command=lambda: button_click('acos('), padx=40, pady=20)
        button_tan.config( text="tan⁻¹", command=lambda: button_click('atan('), padx=40, pady=20)
        button_logb.config( text="log_a(b)", command=lambda: button_click('log('), padx=40, pady=20)
        button_power2.config( text="x³", command=lambda: button_click('^3'), padx=40, pady=20)
        button_root.config( text="∛", command=lambda: button_click('∛('), padx=40, pady=20)
    else:
        button_pi.config(text="π", command=lambda: button_click('π'), padx=40, pady=20)
        button_fact.config(text="!", command=lambda: button_click('!'), padx=40, pady=20)
        button_sin.config(text="sin", command=lambda: button_click('sin('), padx=40, pady=20)
        button_cos.config(text="cos", command=lambda: button_click('cos('), padx=40, pady=20)
        button_tan.config(text="tan", command=lambda: button_click('tan('), padx=40, pady=20)
        button_logb.config(text="log", command=lambda: button_click('log10('), padx=40, pady=20)
        button_power2.config(text="x²", command=lambda: button_click('^2'), padx=40, pady=20)
        button_root.config(text="√", command=lambda: button_click('√('), padx=40, pady=20)
    print(s)


# Create buttons for the calculator
button_1 = tk.Button(window, text="1", command=lambda: button_click('1'), padx=40, pady=20)
button_2 = tk.Button(window, text="2", command=lambda: button_click('2'), padx=40, pady=20)
button_3 = tk.Button(window, text="3", command=lambda: button_click('3'), padx=40, pady=20)
button_4 = tk.Button(window, text="4", command=lambda: button_click('4'), padx=40, pady=20)
button_5 = tk.Button(window, text="5", command=lambda: button_click('5'), padx=40, pady=20)
button_6 = tk.Button(window, text="6", command=lambda: button_click('6'), padx=40, pady=20)
button_7 = tk.Button(window, text="7", command=lambda: button_click('7'), padx=40, pady=20)
button_8 = tk.Button(window, text="8", command=lambda: button_click('8'), padx=40, pady=20)
button_9 = tk.Button(window, text="9", command=lambda: button_click('9'), padx=40, pady=20)
button_0 = tk.Button(window, text="0", command=lambda: button_click('0'), padx=40, pady=20)
button_add = tk.Button(window, text="+", command=lambda: button_click('+'), padx=40, pady=20)
button_sub = tk.Button(window, text="-", command=lambda: button_click('-'), padx=40, pady=20)
button_mul = tk.Button(window, text="×", command=lambda: button_click('×'), padx=40, pady=20)
button_div = tk.Button(window, text="÷", command=lambda: button_click('÷'), padx=40, pady=20)
button_brack1 = tk.Button(window, text="(", command=lambda: button_click('('), padx=40, pady=20)
button_brack2 = tk.Button(window, text=")", command=lambda: button_click(')'), padx=40, pady=20)
button_equal = tk.Button(window, text="=", command = lambda: button_calculate(), padx=40, pady=20)
button_clear = tk.Button(window, text="CLEAR", command=lambda: button_click('clear'), padx=40, pady=20)
button_shf = tk.Button(window, text="SHIFT", command=lambda: shiftb(), padx=40, pady=20)
button_eqn = tk.Button(window, text="Eqn", command=lambda: eqnb(), padx=40, pady=20)
button_quad = tk.Button(window, text="Q", command=lambda: button_click('Q'), padx=40, pady=20)
button_cube = tk.Button(window, text="C", command=lambda: button_click('C'), padx=40, pady=20)

button_pi = tk.Button(window, text="π", command=lambda: button_click('π'), padx=40, pady=20)
button_fact = tk.Button(window, text="!", command=lambda: button_click('!'), padx=40, pady=20)
button_sin = tk.Button(window, text="sin", command=lambda: button_click('sin('), padx=40, pady=20)
button_cos = tk.Button(window, text="cos", command=lambda: button_click('cos('), padx=40, pady=20)
button_tan = tk.Button(window, text="tan", command=lambda: button_click('tan('), padx=40, pady=20)
button_logb = tk.Button(window, text="log", command=lambda: button_click('log10('), padx=40, pady=20)
button_power2 = tk.Button(window, text="x²", command=lambda: button_click('^2'), padx=40, pady=20)
button_root = tk.Button(window, text="√", command=lambda: button_click('√('), padx=40, pady=20)


button_logb.grid(row=1, column=0)
button_power2.grid(row=1, column=1)
button_root.grid(row=1, column=2)
button_pi.grid(row=3, column=2)

button_sin.grid(row=2, column=0)
button_cos.grid(row=2, column=1)
button_tan.grid(row=2, column=2)

button_brack1.grid(row=3, column=0)
button_brack2.grid(row=3, column=1)

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_0.grid(row=7, column=0)
button_clear.grid(row=7, column=2)

button_add.grid(row=8, column=0)
button_sub.grid(row=8, column=1)
button_equal.grid(row=8, column=2)

button_mul.grid(row=9, column=0)
button_div.grid(row=9, column=1)
button_fact.grid(row=9, column=2)
button_shf.grid(row=7, column=1)
button_eqn.grid(row=10, column=0)
button_quad.grid(row=10, column=1)
button_cube.grid(row=10, column=2)


window.mainloop()
