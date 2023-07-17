# Now that you have planned out your tour, you are ready to go! Your next task is to mark all the points on the map
# that you are going to visit. You will be given a string representing some places on the map.
# You have to filter only the valid ones. A valid location is:
# •	Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
# •	After the first "=" or "/" there should be only letters (the first must be upper-case, other letters could be upper
# or lower-case)
# •	The letters must be at least 3
# Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.
# After you have matched all the valid locations, you have to calculate travel points. They are calculated by summing
# the lengths of all the valid destinations that you have found on the map.
# In the end, on the first line, print: "Destinations: {destinations joined by ', '}".
# On the second line, print "Travel Points: {travel_points}".
#
# Input1: =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=
# Output1:
# Destinations: Hawai, Cyprus
# Travel Points: 11
#
# Input2: ThisIs some InvalidInput
# Output2:
# Destinations:
# Travel Points: 0

import re

points = 0
all_destinations = []

data = input()
pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
result = re.finditer(pattern, data)


for destination_ in result:
    destination = destination_.group(2)
    points += len(destination)
    all_destinations.append(destination)

print(f"Destinations: {', '.join(all_destinations)}")
print(f"Travel Points: {points}")
