from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

milk = Thing("Get milk")
obstacle = Thing("Remove the obstacles")
stand = Thing("Stand up")
lunch = Thing("Eat lunch")

fleet.add(milk)
fleet.add(obstacle)
fleet.add(stand)
fleet.add(lunch)

stand.complete()
lunch.complete()

print(fleet)
