from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def three_line(x,y):
    id = canvas.create_line(x, y, 150, 150, fill="#476042", width=3)
    return id

three_line(50, 50)
three_line(250, 50)
three_line(150, 250)

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

root.mainloop()
