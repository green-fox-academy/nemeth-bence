from tkinter import *

class GameObject():

    def __init__(self):
        self.image_size = 72
        self.floor_image = PhotoImage(file = 'assets\Floor.png')
        self.wall_image = PhotoImage(file = 'assets\Wall.png')

    def draw_image(self, x, y, tile):
        id = canvas.create_image(x*self.image_size, y*self.image_size, anchor = NW, image = tile)
        return id

class Character():

    def __init__(self):
        self.hero_image = PhotoImage(file = 'hero-down.gif')
        self.hero_x = 0
        self.hero_y = 0
        self.hero = game.draw_image(self.hero_x, self.hero_y, self.hero_image)

    def move(self, direction):
        y = 0
        x = 0
        if direction == 'up':
            y = y - game.image_size
        if direction == 'right':
            x = x + game.image_size
        if direction == 'down':
            y = y + game.image_size
        if direction == 'left':
            x = x - game.image_size

        canvas.move(self.hero, x, y)

    def on_key_press(press):

        if press.keycode == 38:

        elif press.keycode == 40:

        elif press.keycode == 39:

        elif press.keycode == 37:

        # and lower if the key that was pressed the down arrow
        # draw the box again in the new position
        box.draw(canvas)

        canvas.bind("<KeyPress>", on_key_press)

    # def get_position(self, x, y):
    #     self.position = self.canvas.create_image(x*image_size, y*image_size, image = self.photo)

class GameMap:

    def __init__(self):
        self.game_area = [
        [0, 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0],
        [0, 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0],
        [0, 1 , 1 , 1 , 0 , 1 , 0 , 1 , 1 , 0],
        [0, 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0],
        [1, 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0],
        [0, 1 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0],
        [0, 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0],
        [0, 0 , 0 , 0 , 0 , 1 , 1 , 0 , 1 , 0],
        [0, 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 0],
        [0, 0 , 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0]
        ]

    def create_map(self):
        for i in range(len(self.game_area)):
            for j in range(len(self.game_area[i])):
                if self.game_area [i][j] == 0:
                    game.draw_image(j, i, game.floor_image)
                else:
                    game.draw_image(j, i, game.wall_image)


# class Gameplay():
#         pass


root = Tk()
canvas = Canvas(width = '720', height = '720')

game = GameObject()
map = GameMap ()
map.create_map()
hero = Character()
#hero.move()

canvas.pack()

root.mainloop()
