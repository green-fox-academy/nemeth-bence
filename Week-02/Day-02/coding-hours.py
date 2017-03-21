# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

attendee_daily = 6
weeks = 17
working_hours = 52
weekly_coding = 6*5
week_days = 5

print ("Coding hours per semester are " + str(attendee_daily * week_days * weeks) + " hours.")
print ("Coding hours are " + str(weekly_coding/working_hours * 100) + " percent of working hours.")
