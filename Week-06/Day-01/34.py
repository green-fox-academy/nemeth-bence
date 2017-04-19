numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def SumFunction(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(SumFunction(numbers))
print(SumFunction([5,7,99]))
