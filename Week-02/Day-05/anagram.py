# Create a function named is anagram following your current language's style guide. It should take two strings and return a boolean value depending on whether its an anagram or not.

def anagram(p1, p2):
    list1 = list(p1)
    list2 = list(p2)

    list1.sort()
    list2.sort()

    position = 0
    match = True

    while position < len(p1) and match:
        if list1[position]==list2[position]:
            position = position + 1
        else:
            match = False

    return match

print("Hi, give me two words. I'll tell you, they're anagrams or not: ")
v = input("First word: ")
z = input("Second word: ")

print(anagram(v,z))
