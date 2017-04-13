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
    column = []
    for i in range(size):
        column = [0] * size
        column[i] = 1

        print(column)
    return


matrix(5)
matrix(7)
