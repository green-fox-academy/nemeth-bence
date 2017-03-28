# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

while True:
    try:
        numba = int(input("Give me a number: "))
        print(10/numba)
        break
    except ZeroDivisionError:
        print("fail")
