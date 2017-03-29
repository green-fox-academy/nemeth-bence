from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.
'''def squares(size, color):
    #size = size/2
    draw = canvas.create_rectangle(size, size, size, size, fill=color, width=3)

size = 20
color = ['white', 'black']
step = size/len(color)'''

l1 = [[1,2,3],[4,5,6],[7,8,9]]

d1 = {a:[1,2,3],b:[4,5,6],c:[7,8,9]}

checkerboard = {}

for row in range(15):
    for col in range(15):
        checkerboard[(row,col)] = 0
        color = ['white', 'black']


'''for i in range(len(color)):
squares(size, color[i])
size -= step'''

root.mainloop()
