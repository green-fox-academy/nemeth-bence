from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

box = canvas.create_rectangle(145, 145, 155, 155, fill='lime green')
# draw a green 10x10 square to the center of the canvas.

root.mainloop()
