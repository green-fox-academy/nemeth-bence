from tkinter import *
#import time

root = Tk()
canvas = Canvas(root, width='400', height='400' , bg='#00313f' )
canvas.pack()


def draw_three_lines(x1, y1, x2, y2, n):
    if n == 1:

        line = canvas.create_line(x1, y1, x2, y2, fill='#ffd800')
        line = canvas.create_line(x1 + (x2-x1)/2, y1 + (y2-y1)/2, x1 +(y2-y1)/4, y2, fill='#ffd800')
        line = canvas.create_line(x1 + (x2-x1)/2, y1 + (y2-y1)/2, x1 -(y2-y1)/4, y2, fill='#ffd800')

    else:
        line = canvas.create_line(x1, y1, x2, y2, fill='#ffd800')
        line = canvas.create_line(x1 + (x2-x1)/2, y1 + (y2-y1)/2, x1 +(y2-y1)/4, y2, fill='#ffd800')
        line = canvas.create_line(x1 + (x2-x1)/2, y1 + (y2-y1)/2, x1 -(y2-y1)/4, y2, fill='#ffd800')
        draw_three_lines(x2, y2, x2, y2+ (y2-y1)*2, n-1)
        draw_three_lines(x1 +(y2-y1)/4, y2, x2 + (y2-y1)/2, y2+ (y2-y1)*2, n-1)
        draw_three_lines(x1 -(y2-y1)/4, y2, x2 - (y2-y1)/2, y2 + (y2-y1)*2, n-1)

draw_three_lines(200, 350, 200, 300, 5)

root.mainloop()
