import tkinter as tk
import math as Math
from datetime import datetime as Time
import psutil

def prseed():
    return Math.ceil(Time.now().second * 18.256 + Time.now().microsecond * 0.02125 + get_environment_v() % 7)

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

for i in range(6000):
    C.append(f(i*seed + 1))

normalize()

def generate():
    label.config(text = C[prseed() % 6000])
    copyButton.config(state="normal")

def copy():
    root.clipboard_clear()
    root.clipboard_append(label.cget("text"))

def enter(event):
    generate()

root = tk.Tk()
root.title("Random Number Generator")
root.iconbitmap("C:/Users/Ανδρέας/FunProjects/temp/icon.ico")
root.geometry("400x180")

label = tk.Label(root, text="Click 'Generate' to start")
label.pack(pady=10)
label2 = tk.Label(root, text="Seed = " + str(seed), font=("Calibri", 8))
label2.pack(pady=4)
button = tk.Button(root, text="Generate", command=lambda: generate(), width=13, height=2, font=("Calibri", 12), bg="lightblue", fg="black")
button.pack(pady=10)
copyButton = tk.Button(root, text="Copy To Clipboard", command=lambda: copy(), state="disabled", bg="#F3F9EE")
copyButton.pack()

root.bind("<Return>", enter)

root.mainloop()