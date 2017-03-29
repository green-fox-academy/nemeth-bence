from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def center_squares(size):
    draw = canvas.create_rectangle(150, 150, size, size, width=3)
    return draw

center_squares(100)
center_squares(75)
center_squares(50)


root.mainloop()
