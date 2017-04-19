# create a function that returns it's input factorial

def Factorio(any):
    f = 1
    for i in range(1, any + 1):
        f *= i
    return f

print(Factorio(4))

def Factorio2(num):
    if num == 1:
        return 1
    else:
        return Factorio2(num - 1) * num

print(Factorio2(4))
