
queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

def security_check(list):
    watchlist = []
    festivalgoers = []
    security_alcohol_loot = 0
    for i in range(len(list)):
        festivalgoers.append(list[i]['name'])
    for i in range(len(list)):
        for key in list[i]:
            if list[i]['guns'] != 0:
                list[i]['guns'] = 0
                watchlist.append(list[i]['name'])
                festivalgoers.remove(list[i]['name'])
            if list[i]['alcohol'] != 0:
                security_alcohol_loot += list[i]['alcohol']
                list[i]['alcohol'] = 0
    print(watchlist)
    print(security_alcohol_loot)
    print(festivalgoers)

security_check(queue)
