# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

n = int (input("Gimme a number, and it counts from 1 to it: "))

def num_adder(n):
    if n == 0:
        return 0
    else:
        return num_adder(n-1) + n

print(num_adder(n))
