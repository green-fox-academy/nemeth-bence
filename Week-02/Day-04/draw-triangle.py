# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

number = int(input("Milyen magas legyen a piramisod? "))
height = ""

for i in range(0,number):
    height += "*"
    print(height)
