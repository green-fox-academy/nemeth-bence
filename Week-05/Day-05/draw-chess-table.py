# Create a program that draws a chess table like this
#
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
#

a = 4
b = 8

if a % 2 == 0 and b % 2 == 0:
    for i in range (0, a):
        print((a) * "% ")
        print((a) * " %")
