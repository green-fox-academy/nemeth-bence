from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

line = canvas.create_line(100, 100, 200, 100, fill='red')
line = canvas.create_line(200, 100, 200, 200, fill='green')
line = canvas.create_line(200, 200, 100, 200, fill='blue')
line = canvas.create_line(100, 200, 100, 100, fill='yellow')

# draw a box that has different colored lines on each edge.

root.mainloop()
