# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts listOfNumbers as an input
# it should return "true" if it contains all, otherwise print "false"

listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]

check = [4, 8, 12, 16]

def checklist(small, biglist):
    for number in small:
        if number in biglist:
            return(True)
        else:
            print(False)

print(checklist(check, listOfNumbers))
