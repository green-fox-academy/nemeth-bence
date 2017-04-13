import random

class Pirate:

    def __init__(self):
        self.level_rum = 0
        self.alive = True
        self.passed_out = False

    def drink_some_rum(self):
        if self.alive == True:
            self.level_rum += 1
        else:
            print("He's dead.")

    def hows_it_going_mate(self):
        if self.alive == True:
            if self.level_rum < 4:
                print("Pour me anudder!")
            else:
                print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
                self.passed_out = True
        else:
            print("He's dead.")


    def die(self):
        self.alive == False

    def pass_out(self):
        self.passed_out: True
