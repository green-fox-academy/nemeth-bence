from tkinter import *

class GameObject():

    def __init__(self):
        self.image_size = 72
        #self.character = character
        #self.move = move
        #self.position = position
        self.floor_image = PhotoImage(file = 'assets\Floor.png')
        self.wall_image = PhotoImage(file = 'assets\Wall.png')
        # self.draw_image(2, 5, self.floor_image)
        # self.draw_image(6, 4, self.wall_image)


    def draw_image(self, x, y, tile):
        self.image = canvas.create_image(x*self.image_size, y*self.image_size, image = tile)

class Character():

    def __init__(self):
        self.hero_image = PhotoImage(file = 'assets\hero-down.png')
        self.hero_x = 36
        self.hero_y = 36
        game.draw_image(self.hero_x, self.hero_y, self.hero_image)

        #self.hero_image = PhotoImage(file = 'assets\hero_down.png')

    # def get_position(self, x, y):
    #     self.position = self.canvas.create_image(x*image_size, y*image_size, image = self.photo)

    # def move(self):

# class Wall(GameObject):
#     def __init__(self,root,canvas,background="wall.gif"):
#         super().__init__(root,canvas,background)
#
# class Floor(GameObject):
#     def __init__(self,root,canvas,background="floor.gif"):
#         super().__init__(root,canvas,background)
#
#
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
                    game.draw_image(j + 0.5, i + 0.5, game.floor_image)
                else:
                    game.draw_image(j + 0.5, i + 0.5, game.wall_image)





    # def crt_objts_map(self):
    #     for i in range(len(self.game_area)):
    #         for j in range(len(self.game_area[i])):
    #             if self.game_area[i][j] == 1:
    #                 self.wall.create_object(i*72,j*72)
    #             if self.game_area[i][j] == 0:
    #                 self.floor.create_object(i*72,j*72)
#
#
# class Gameplay():
#         pass


root = Tk()
canvas = Canvas(width = '720', height = '720')

game = GameObject()
map = GameMap ()
map.create_map()
hero = Character()

canvas.pack()

root.mainloop()
