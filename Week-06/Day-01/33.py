ag = 'kuty'
# write a function that gets a string as an input
# and appends an 'a' character to its end

def stringer(appender):
    return appender + 'a'

rf = stringer(ag)

print(rf)


ag2 = ['rep', 'macsk', 'cic', 'alm', 'Ann', 'kacs']

for i in range(len(ag2)):
    ag2[i] = stringer(ag2[i])

print(ag2)
