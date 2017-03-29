from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

box = canvas.create_rectangle(85, 85, 215, 215, fill='black')
box = canvas.create_rectangle(105, 105, 195, 195, fill='white')
box = canvas.create_rectangle(125, 125, 175, 175, fill='yellow')
box = canvas.create_rectangle(145, 145, 155, 155, fill='pink')

# draw four different size and color rectangles.

root.mainloop()
