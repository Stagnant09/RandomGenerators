import tkinter as tk
import math as Math
from datetime import datetime as Time
import psutil
import re

def digits(n):
    if n == 0:
        return 1
    else:
        return int(Math.log(n, 10)) + 1

def prseed():
    return Math.ceil(Time.now().second * 18.256 + Time.now().microsecond * 0.02125 + get_environment_v() % 7)

def prseed_2():
    return Math.ceil(Time.now().second * 1.25 + Time.now().microsecond * 0.00025 + get_environment_v() % 15)

def get_environment_v():
    return Math.floor(psutil.virtual_memory().percent * 100)

C = []
seed = Math.ceil(Time.now().second * 1.25 + Time.now().microsecond * 0.00025 + get_environment_v() % 15)

def f(x):
    i = 5*x + 1 % seed
    j = 6*x + 2 % seed
    k = 10*seed + 3 % seed
    l = 3*x
    m = 3*x + 1
    n = Math.floor(Math.pi * x)
    q = Math.floor(Math.e * x / 7)
    r = Math.floor(Math.log(x, 10)*Math.e) + 1
    s = Math.floor(Math.log(x, 2)*100) + (x // 7)
    t = Math.floor(Math.log(x, 2)*10) + (x // 11)
    u = Math.floor(Math.log(x, 2)*10) + (x // 13)
    v = Math.floor(Math.log(x, 2)*10) + (x // 17)
    abs_dis = [abs(x-i), abs(x-j), abs(x-k), abs(x-l), abs(x-m), abs(x-n), abs(x-q), abs(x-r), abs(x-s), abs(x-t), abs(x-u), abs(x-v)]
    return Math.floor((min(abs_dis)+max(abs_dis))/ (x % 3 + 1)) + (i+j)*(min(abs(x-i)-100, abs(x-j)-100))

def normalize():
    for i in range(1000):
        if (i % 3 == 0 or i % 11 == 0):
            C[i] = Math.floor(C[i] / 100)
        if i % 5 == 0:
            C[i] = Math.floor(C[i] / 1000)
        if i % 6 == 0:
            C[i] = Math.floor(C[i] / 10000)
        if i % 50 == 0 and i % 20 == 0:
            C[i] = Math.floor(C[i] / 2)
        if i % 54 == 0 or i % 12 == 0:
            C[i] = Math.floor(C[i] / 10) + Math.floor(Math.pi * 10**(i%100) % 10)
        if i % 133 == 0 or i % 177 == 0:
            C[i] = Math.floor(C[i] / 1000)
        if C[i] == 0:
            #Set as C[i] the i-th digit of pi
            C[i] = Math.floor(Math.pi * 10**(i%100) % 10)
        if C[i] < 0:
            C[i] = abs(C[i])

def make_C():
    for i in range(6000):
        C.append(f(i*seed + 1))

make_C()
normalize()

def show_warning(message):
    warning_window = tk.Toplevel(root)
    warning_window.title("Warning")
    warning_window.iconbitmap("C:/Users/Ανδρέας/FunProjects/temp/icon2.ico")
    warning_label = tk.Label(warning_window, text=message)
    warning_label.pack(padx=15, pady=10)
    close_button = tk.Button(warning_window, text="Got It!", command=warning_window.destroy)
    close_button.pack(padx=10, pady=10)

def generate():
    if value_of_is_improper(spinbox.get()) and checkbox_var.get() == True:
        show_warning("Wrong input. Maximum value must be an integer greater than 0.")
        return
    if C[prseed() % 6000] > int(spin_b_v) and checkbox_var.get() == True:
        label.config(text = fixed_text(C[prseed() % 6000], int(spinbox.get())))
    else:   
        label.config(text = C[prseed() % 6000])
    copyButton.config(state="normal")

def copy():
    root.clipboard_clear()
    root.clipboard_append(label.cget("text"))

def enter(event):
    generate()

def value_of_is_improper(x):
    if x == "":
        return True
    if re.match("^[0-9]+$", x) == None:
        return True
    if int(x) <= 0:
        return True
    return False

spin_b_v = 0

def on_checkbox_click():
    pass

def on_spinbox_change():
    global spin_b_v
    spin_b_v = spinbox.get()

def fixed_text(n, max_v):
    while digits(n) > digits(max_v) or n > max_v:
        n = n // 10
    return n

def reset_seed():
    seed = prseed_2()
    label2.config(text="Seed = " + str(seed))

root = tk.Tk()
root.title("Random Number Generator")
root.iconbitmap("C:/Users/Ανδρέας/FunProjects/temp/icon.ico")
root.geometry("390x250")
root.resizable(width=False, height=False)

checkbox_var = tk.BooleanVar()

label = tk.Label(root, text="Click 'Generate' to start")
label.pack(pady=10)
label2 = tk.Label(root, text="Seed = " + str(seed), font=("Calibri", 8))
label2.pack(pady=4)
button = tk.Button(root, text="Generate", command=lambda: generate(), width=13, height=2, font=("Calibri", 12), bg="lightblue", fg="black")
button.pack(pady=8)
copyButton = tk.Button(root, text="Copy To Clipboard", command=lambda: copy(), state="disabled", bg="#F3F9EE")
copyButton.pack()
button2 = tk.Button(root, text="Reset Seed", command=lambda: reset_seed(), width=8, height=1)
button2.pack(pady=(6,0))
checkbox = tk.Checkbutton(root, text="Set maximum value as", variable=checkbox_var, command=on_checkbox_click)
checkbox.pack(side=tk.LEFT, padx=(44,0))
spinbox = tk.Spinbox(root, from_=0, to=10000000000000000000, increment=100000, textvariable="Maximum Value", command=on_spinbox_change)
spinbox.pack(side=tk.RIGHT, padx=(0,44))


root.bind("<Return>", enter)

root.mainloop()