# Define a recursive fibonacci(n) method that returns the nth # fibonacci number, with n=0 representing the start of the sequence.



#0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci (n):

    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(0))

def fibonacci (n):

    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(7))
