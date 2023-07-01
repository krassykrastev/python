# The force users struggle to remember which side is the different force users from because they switch them too often.
# So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
# • If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# • Only if there is no such force user in any force side -> add the force user to the corresponding side.
# • If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# • If there is such force user already -> change their side.
# • If there is no such force user in any force side -> add the force user to the corresponding force side.
# • If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# • Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side.
# For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information.
# Input / Constraints
# • The input comes in the form of commands in one of the formats specified above.
# • The input ends when you receive the command "Lumpawaroo".
# Output
# • As output for each force side, you must print all the force users.
# • The output format is:
# "Side: {force_side}, Members: {force_users_count}
# ! {force_user1}
# © SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 9 of 10
# ! {force_user2}
# …
# ! {force_userN}"
# • In case there are NO force users on a side, don't print this side.
#
# Input1:
# Light | Peter
# Dark | Kim
# Light | Kim
# Lumpawaroo
#
# Output1:
# Side: Light, Members: 1
# ! Peter
# Side: Dark, Members: 1
# ! Kim
#
# Input2:
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo
#
# Output2:
# Ivan Ivanov joins the Lighter side!
# DCay joins the Lighter side!
# Side: Lighter, Members: 3
# ! Royal
# ! Ivan Ivanov
# ! DCay

force_book_users = {}
force_book_side = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_user in force_book_users:
            continue

        force_book_users[force_user] = force_side
        if force_side not in force_book_side:
            force_book_side[force_side] = 1
        else:
            force_book_side[force_side] += 1
    elif "->" in command:
        command = command.split(" -> ")
        force_side = command[1]
        force_user = command[0]
        if force_user in force_book_users:
            old_force_book_side = force_book_users[force_user]
            force_book_side[old_force_book_side] -= 1
            del force_book_users[force_user]
        force_book_users[force_user] = force_side
        if force_side not in force_book_side:
            force_book_side[force_side] = 0
        force_book_side[force_side] += 1

        print(f"{force_user} joins the {force_side} side!")

for side, count_of_members in force_book_side.items():
    if count_of_members > 0:
        print(f"Side: {side}, Members: {count_of_members}")
        for user_, side_ in force_book_users.items():
            if side_ == side:
                print(f"! {user_}")

# another solution
# force_book = {}
#
# command = input()
#
# while command != "Lumpawaroo":
#     if "|" in command:
#         side, user = command.split(" | ")
#         force_book[side] = force_book.get(side, [])
#         user_exists = False
#         for side_, users in force_book.items():
#             if user in users:
#                 user_exists = True
#         if not user_exists:
#             force_book[side].append(user)
#
#     elif "->" in command:
#         user, side = command.split(" -> ")
#         user_exists = False
#         for side_, users in force_book.items():
#             if user in users:
#                 which_side = side_
#                 user_exists = True
#         if user_exists:
#             force_book[which_side].remove(user)
#         force_book[side] = force_book.get(side, [])
#         force_book[side].append(user)
#         print(f"{user} joins the {side} side!")
#     command = input()
# 
# for side, users in force_book.items():
#     if users:
#         print(f"Side: {side}, Members: {len(users)}")
#         for user in users:
#             print(f"! {user}")