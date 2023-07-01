# Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of
# taking all the submissions and analyzing them properly. You should collect all the submissions and print the
# final results and statistics about each language in which the participants submitted their solutions.
# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished".
# You should store each username and their submissions and points. If a student has two or more submissions for the same language,
# save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned".
# In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions
# for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# • Print the exam results for each participant
# • After that, print each language in the format shown above
#
# Input1:
# Peter-Java-84
# George-C#-84
# George-C#-70
# Katy-C#-94
# exam finished
#
# Output1:
# Results:
# Peter | 84
# George | 84
# Katy | 94
# Submissions:
# Java - 1
# C# - 3
#
# Input2:
# Peter-Java-91
# George-C#-84
# Katy-Java-90
# Katy-C#-50
# Katy-banned
# exam finished
#
# Output2:
# Results:
# Peter | 91
# George | 84
# Submissions:
# Java - 2
# C# - 2

results = {}
submissions = {}

while True:
    current_result = input().split("-")
    if len(current_result) == 1: # end the cycle
        break
    elif len(current_result) == 2: # someone is banned
        name = current_result[0]
        del results[name]
    elif len(current_result) == 3: # we got points as input
        name = current_result[0]
        current_language = current_result[1]
        current_points = int(current_result[2])
        if name not in results:
            results[name] = 0
        if results[name] < current_points:
            results[name] = current_points
        if current_language not in submissions:
            submissions[current_language] = 0
        submissions[current_language] += 1

print("Results:")
for user_name, points in results.items():
    print(f"{user_name} | {points}")
print("Submissions:")
for language, submission_count in submissions.items():
    print(f"{language} - {submission_count}")