# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

attendee = 6
semester = 17
work_hours = 52
coding_hours = (semester*5)*attendee

print(coding_hours)
print((coding_hours/(work_hours*semester))*100)
