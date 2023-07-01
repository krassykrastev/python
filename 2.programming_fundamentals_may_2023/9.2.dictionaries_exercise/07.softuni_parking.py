# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work.
# It can only receive users' data, but it doesn't know what to do with it.
# Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# • "register {username} {license_plate_number}":
#   o The system only supports one car per user at the moment, so if a user tries to register another license plate using
#   the same username, the system should print: "ERROR: already registered with plate number {license_plate_number}"
#   o If the check above passes successfully, the user should be registered, so the system should print:
#   "{username} registered {license_plate_number} successfully"
# • "unregister {username}":
#   o If the user is not present in the database, the system should print: "ERROR: user {username} not found"
#   o If the check above passes successfully, the system should print: "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license plates in the format:
# • "{username} => {license_plate_number}"
# Input
# • First line: n - number of commands - integer
# • Next n lines: commands in one of the two possible formats:
#   o Register: "register {username} {license_plate_number}"
#   o Unregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.
#
# Input1:
# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
#
# Output1:
# John registered CS1234JS successfully
# George registered JAVA123S successfully
# Andy registered AB4142CD successfully
# Jesica registered VR1223EE successfully
# Andy unregistered successfully
# John => CS1234JS
# George => JAVA123S
# Jesica => VR1223EE
#
# Input2:
# 4
# register Jony AA4132BB
# register Jony AA4132BB
# register Linda AA9999BB
# unregister Jony
#
# Output2:
# Jony registered AA4132BB successfully
# ERROR: already registered with plate number AA4132BB
# Linda registered AA9999BB successfully
# Jony unregistered successfully
# Linda => AA9999BB
#
# Input3:
# 6
# register Jacob MM1111XX
# register Anthony AB1111XX
# unregister Jacob
# register Joshua DD1111XX
# unregister Lily
# register Samantha AA9999BB
#
# Output3:
# Jacob registered MM1111XX successfully
# Anthony registered AB1111XX successfully
# Jacob unregistered successfully
# Joshua registered DD1111XX successfully
# ERROR: user Lily not found
# Samantha registered AA9999BB successfully
# Anthony => AB1111XX
# Joshua => DD1111XX
# Samantha => AA9999BB

parking = {}
number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        user_name = command[1]
        license_plate = command[2]
        if user_name in parking:
            print(f"ERROR: already registered with plate number {parking[user_name]}")
        else:
            print(f"{user_name} registered {license_plate} successfully")
            parking[user_name] = license_plate
    elif command[0] == "unregister":
        user_name = command[1]
        if user_name not in parking:
            print(f"ERROR: user {user_name} not found")
        else:
            print(f"{user_name} unregistered successfully")
            del parking[user_name]

for user, plate in parking.items():
    print(f"{user} => {plate}")