from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]


def squares(x,y):
    square = canvas.create_rectangle(x, x, y, y, fill='purple', width=1)

x = 10
y = 20

for i in range(19):
    squares(x, y)
    x = y
    y += 10


root.mainloop()
