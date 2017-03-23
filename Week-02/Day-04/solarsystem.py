# Saturn is missing from the planetList
# Insert it into the correct position

planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"]

new_planetList = []

for p in range(len(planetList)):
    if planetList[p] == "Jupiter":
        new_planetList.append(planetList[p])
        new_planetList.append("Saturn")
    else:
        new_planetList.append(planetList[p])

for l in new_planetList:
    print(l)
