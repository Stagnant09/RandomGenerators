import tkinter as tk
import math as Math
from datetime import datetime as Time
import psutil
import platform, GPUtil
import re

x1, y1 = 60, 60  # Top-left corner
x2, y2 = 330, 330  # Bottom-right corner
#Calculate center + radius
center_x = (x1+x2)/2
center_y = (y1+y2)/2
R = abs(center_x - x1)

def get_GPU_stats():
    return GPUtil.getGPUs()[0].memoryUsed + GPUtil.getGPUs()[0].temperature

GPU = get_GPU_stats()

def get_environment_v():
    global GPU
    if (Time.now().microsecond*100) % 50 < 2:
        GPU = get_GPU_stats()
    return Math.floor(psutil.virtual_memory().percent * 100) + Math.pi*10**(psutil.virtual_memory().percent*1.2 %100) % 10 + GPU*0.1

def prseed():
    return Math.ceil((Time.now().second * 2.016 + Time.now().microsecond * 0.12455 + 3*Time.now().microsecond*0.03*Math.pi*10**(Time.now().microsecond%100) % 10) + get_environment_v()*0.25 % 360)

def create_point(angle, radius, center_x, center_y):
    return (Math.cos(angle) * radius + center_x, Math.sin(angle) * radius + center_y)

def generate():
    global R, center_x, center_y
    print("Generating...", R, center_x, center_y)
    dot_size = 3
    point_x, point_y = create_point(Math.radians(prseed() % 360), R, center_x, center_y)
    print(point_x, point_y)
    canvas.create_oval(point_x - dot_size, point_y - dot_size, point_x + dot_size, point_y + dot_size, fill="red")

def enter(event):
    generate()

root = tk.Tk()
root.title("Random Circle Point Generator")
root.iconbitmap("C:/Users/Ανδρέας/FunProjects/Random Generator/icon.ico")
root.geometry("460x460")
root.resizable(width=False, height=False)

button = tk.Button(root, text="Generate", command=generate)
button.pack(pady=(10, 0))

canvas = tk.Canvas(root, width=370, height=370)
canvas.pack()


canvas.create_oval(x1, y1, x2, y2, outline="black", fill="lightblue")

root.bind("<Return>", enter)

root.mainloop()