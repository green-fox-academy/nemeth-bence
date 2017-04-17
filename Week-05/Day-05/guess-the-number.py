# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one of the following:
#
# The stored number is higher
# The stored number is lower
# You found the number: 8

import random
a = int(random.randrange(1, 666))
#print(a)

guess = int(input("I've a chosen number from 0 to 666, try to find it: "))

while a != guess:
    if guess > a:
        print("The stored number is lower")
        guess = int(input("Guess again: "))

    else:
        print("The stored number is higher")
        guess = int(input("Guess again: "))

print("You found the number:" + str(a))
