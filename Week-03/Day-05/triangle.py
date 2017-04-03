from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='400', height='400')
canvas.pack()

def draw_triangle(x, y, size):
    triangle = canvas.create_polygon(x, y, x + size, y, (x + size)/2, y + size, fill= "white", outline="black", width=2)

def recursive_something(x, y, size):
    draw_triangle(x, y, size)
    time.sleep(0.1)
    canvas.update()
    if size > 10:
        recursive_something(x - x/3, y - y/3, size/3)
        recursive_something(x - x*3, y - y*3, size*3)
        #recursive_something(x+2/3*size, y, size/3)
        #recursive_something(x, y+2/3*size, size/3)

recursive_something(10, 10, 380)

root.mainloop()
