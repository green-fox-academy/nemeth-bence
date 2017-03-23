# Create a program that asks for a number and prints the multiplication table with that number

print("Mit akarsz szorozni?")
szorzando = int(input())

for i in range(1, 11):
    print(i,'*',szorzando,'=',i*szorzando)
