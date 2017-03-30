# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

b = 3
n = 3

def power(b, n):
    if n == 1:
        return b
    else:
        return b * power(b, n-1)

print (power(b,n))
