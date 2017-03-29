from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def center_squares(size, color):
    draw = canvas.create_rectangle(150, 150, 150 + size, 150 + size, fill=color, width=3)
    return draw

center_squares(100, 'red')
center_squares(75, 'green')
center_squares(50, 'blue')

root.mainloop()
