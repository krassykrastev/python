# Here comes the final and the most interesting part – the Final ranking of the candidate-interns.
# The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni.
# Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until
# you receive "end of contests". Save that data because you will need it later. After that you will receive other type
# of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions".
# Here is what you need to do.
# • Check if the contest is valid (It is considered valid if you received it in the first type of input)
# • Check if the password is correct for the given contest
# • If the contest and the password is valid, save the user with the contest they take part in (a user can take part in
# many contests) and the points the user has in the given contest. If you receive the same contest and the same user
# update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they
# participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all
# students ordered by their names. For each user print each contest with the points in descending order. See the examples.
# Input
# • Strings in format "{contest}:{password for contest}" until the "end of contests" command.
# There will be no case with two equal contests
# • Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# • There will be no case with 2 or more users with same total points!
# Output
# • On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# • Then print all students ordered as mentioned above in format:
# "{user_name1}
# # {contest1} -> {points}
# # {contest2} -> {points}
# …
# # {contestN} -> {points}"
# Constraints
# • The strings may contain any ASCII character except from (:, =, >).
# • The numbers will be in range [0 - 10000].
# • Second input is always valid.
#
# Input1:
# Part One Interview:success
# JS Fundamentals:fundExam
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>wrong_pass=>Teo=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>Kay=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# JS Fundamentals=>fundExam=>Tanya=>400
# end of submissions
#
# Output1:
# Best candidate is Tanya with total 1350 points.
# Ranking:
# Nikola
# # C# Fundamentals -> 200
# # Part One Interview -> 120
# Tanya
# # JS Fundamentals -> 400
# # Algorithms -> 380
# # C# Fundamentals -> 350
# # Part One Interview -> 220
#
# Input2:
# Java Advanced:funpass
# Part Two Interview:success
# Math Concept:asdasd
# Java Web Basics:forrF
# end of contests
# Math Concept=>ispass=>Monika=>290
# Java Advanced=>funpass=>Simona=>400
# Part Two Interview=>success=>Drago=>120
# Java Advanced=>funpass=>Petyr=>90
# Java Web Basics=>forrF=>Simona=>280
# Part Two Interview=>success=>Petyr=>0
# Math Concept=>asdasd=>Drago=>250
# Part Two Interview=>success=>Simona=>200
# end of submissions
#
# Output2:
# Best candidate is Simona with total 880 points.
# Ranking:
# Drago
# # Math Concept -> 250
# # Part Two Interview -> 120
# Petyr
# # Java Advanced -> 90
# # Part Two Interview -> 0
# Simona
# # Java Advanced -> 400
# # Java Web Basics -> 280
# # Part Two Interview -> 200
contest_and_pass = {}
users = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")

    contest_and_pass[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    points = int(points)
    if contest in contest_and_pass and password == contest_and_pass[contest]:
        if username not in users:
            users[username] = {contest: points}
        else:
            if contest not in users[username]:
                users[username][contest] = points
            if users[username][contest] < points:
                users[username][contest] = points

best_score = 0
best_candidate = ""

for user in users:
    current_score = sum(users[user].values())
    if current_score > best_score:
        best_score = current_score
        best_candidate = user

print(f"Best candidate is {best_candidate} with total {best_score} points.")
print("Ranking:")

sorted_users = dict(sorted(users.items(), key=lambda x: x[0]))

for name in sorted_users:
    print(name)
    sorted_contests = sorted(sorted_users[name].items(), key=lambda x: -x[1])
    for i in range(len(sorted_contests)):
        print(f"#  {sorted_contests[i][0]} -> {sorted_contests[i][1]}")