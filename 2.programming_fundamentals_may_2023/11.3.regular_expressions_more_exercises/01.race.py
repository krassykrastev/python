# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given some info which will be
# some alphanumeric characters. In between them you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and the sum of the digits is
# the distance he ran. So here we have George who ran 29 km. Store the information about the person only if
# the list of racers contains the name of the person. If you receive the same person more than once just
# add the distance to his old distance. At the end print the top 3 racers ordered by distance in descending
# in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"
#
# Input1:
# George, Peter, Bill, Tom
# G4e@55or%6g6!68e!!@
# R1@!3a$y4456@
# B5@i@#123ll
# G@e54o$r6ge#
# 7P%et^#e5346r
# T$o553m&6
# end of race
#
# Output1:
# 1st place: George
# 2nd place: Peter
# 3rd place: Tom

import re

pattern = "([a-zA-Z]+)|([0-9])"
name_and_distance = {}

list_of_participants = input().split(", ")

while True:
    command = input()

    if command == "end of race":
        break

    matches = re.findall(pattern, command)

    name = ""
    sum_of_distance = 0

    for match in matches:

        if match[0]:
            name += match[0]

        if match[1]:
            sum_of_distance += int(match[1])

    if name in list_of_participants:
        if name not in name_and_distance:
            name_and_distance[name] = sum_of_distance
        else:
            name_and_distance[name] += sum_of_distance

name_and_distance_sorted = dict(sorted(name_and_distance.items(), key=lambda x: -x[1]))

rank = 0
current_rank = ""

for name in name_and_distance_sorted.keys():
    rank += 1
    if rank > 3:
        break
    if rank == 1:
        current_rank = "1st"
    elif rank == 2:
        current_rank = "2nd"
    elif rank == 3:
        current_rank = "3rd"
    print(f"{current_rank} place: {name}")
