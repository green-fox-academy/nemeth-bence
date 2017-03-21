# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000

x = 30
y = 40
z = 50

print ("Surface Area: " + str(x+y + y+z + x+z))
print ("Volume: " + str(x*y*z))
