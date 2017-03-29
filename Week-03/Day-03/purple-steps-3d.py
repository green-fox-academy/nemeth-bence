from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]


def squares(x,y):
    square = canvas.create_rectangle(x, x, y, y, fill='purple', width= 1)

for i in range(6):

    squares(10 + (1.8**i)*4, 10 + 1.8**(i+1)*4)

root.mainloop()
