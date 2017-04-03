# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

def matrix(size):
    oszlop = []
    for i in range(size):
        oszlop = [0] * size
        oszlop[i] = 1

        print(oszlop)
    return


matrix(5)
matrix(7)
