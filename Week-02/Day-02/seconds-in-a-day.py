current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables

TotalDaySec = 24*60*60
Hours = 14*60*60
Mins = 34*60
Secs = 42

print (TotalDaySec)
print (Hours)
print (Mins)

print ("Remaining seconds from the day: " + str (TotalDaySec - (Hours + Mins + Secs)))
