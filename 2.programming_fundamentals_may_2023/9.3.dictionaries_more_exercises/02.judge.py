# You know the judge system, right?! Your job is to create a program similar to the Judge system.
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number.
# You need to keep track of every contest and points of each user:
# • If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
# • Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time".
# At that point, you should print each contest in order of input, for each contest print the participants ordered by points
# in descending order, then ordered by name in ascending order. After that, you should print individual statistics for
# every participant ordered by total points in descending order, and then by alphabetical order.
# Input / Constraints
# • The input comes in the form of commands in one of the formats specified above.
# • Username and contest name always will be one word.
# • Points will be an integer in the range [0, 1000].
# • There will be no invalid input lines.
# • If all sorting criteria fail, the order should be by order of input.
# • The input ends when you receive the command "no more time".
# Output
# • The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# • After you print all contests, print the individual statistics for every participant.
# • The output format is:
# "Individual standings:
# 1. {username1} -> {total_points}
# 2. {username} -> {total_points}
# …
# {N}. {username} -> {total_points}"
#
# Input1:
# Peter -> Algo -> 400
# George -> Algo -> 300
# Simo -> Algo -> 200
# Peter -> DS -> 150
# Mariya -> DS -> 600
# no more time
#
# Output1:
# Algo: 3 participants
# 1. Peter <::> 400
# 2. George <::> 300
# 3. Simo <::> 200
# DS: 2 participants
# 1. Mariya <::> 600
# 2. Peter <::> 150
# Individual standings:
# 1. Mariya -> 600
# 2. Peter -> 550
# 3. George -> 300
# 4. Simo -> 200
#
# Input2:
# Peter -> OOP -> 350
# George -> OOP -> 250
# Simo -> Advanced -> 600
# George -> OOP -> 300
# Prakash -> OOP -> 300
# Prakash -> Advanced -> 250
# Ani -> JSCore -> 400
# no more time
#
# Output2:
# OOP: 3 participants
# 1. Peter <::> 350
# 2. George <::> 300
# 3. Prakash <::> 300
# Advanced: 2 participants
# 1. Simo <::> 600
# 2. Prakash <::> 250
# JSCore: 1 participants
# 1. Ani <::> 400
# Individual standings:
# 1. Simo -> 600
# 2. Prakash -> 550
# 3. Ani -> 400
# 4. Peter -> 350
# 5. George -> 300

result = {}
individual_standings = {}

while True:
    command = input()

    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in result:
        result[contest] = {username: points}
    if username not in result[contest]:
        result[contest][username] = points
    if result[contest][username] < points:
        result[contest][username] = points

for contest, username in result.items():
    print(f"{contest}: {len(username)} participants")

    for index in range(len(username)):
        sorted_points = sorted(username.items(), key=lambda sort: (-sort[1], sort[0]))
        print(f"{index + 1}. {sorted_points[index][0]} <::> {sorted_points[index][1]}")

        if sorted_points[index][0] not in individual_standings:
            individual_standings[sorted_points[index][0]] = sorted_points[index][1]

        else:
            individual_standings[sorted_points[index][0]] += sorted_points[index][1]

sorted_individual_standings = sorted(individual_standings.items(), key=lambda points: (-points[1], points[0]))

print("Individual standings:")

for index in range(len(sorted_individual_standings)):
    print(f"{index + 1}. {sorted_individual_standings[index][0]} -> {sorted_individual_standings[index][1]}")