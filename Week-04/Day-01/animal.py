'''Create Animal class
Every animal has a hunger value, which is a whole number
Every animal has a thirst value, which is a whole number
when creating a new animal object these values are created with the default 50 value
Every animal can eat() which decreases their hunger by one
Every animal can drink() which decreases their thirst by one
Every animal can play() which increases both by one'''

class Animal:
    hunger = 50
    thirst = 50

    def eat(self):
        print('More hungry.')
        self.hunger -= 1

    def drink(self):
        print('More thirsty.')
        self.thirst -= 1

    def play(self):
        print('Life power!')
        self.thirst += 1
        self.hunger += 1


snake = Animal()

snake.eat()
snake.play()

print(snake.hunger)
