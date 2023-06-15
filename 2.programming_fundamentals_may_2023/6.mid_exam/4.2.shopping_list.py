# It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
# Input
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.
# Constraints
# •	There won't be any duplicate items in the initial list
# Output
# •	Print the list with all the groceries, joined by ", ":
# "{firstGrocery}, {secondGrocery}, … {nthGrocery}"
#
# Input1:
# Tomatoes!Potatoes!Bread
# Unnecessary Milk
# Urgent Tomatoes
# Go Shopping!
#
# Output1: Tomatoes, Potatoes, Bread
#
# Input2:
# Milk!Pepper!Salt!Water!Banana
# Urgent Salt
# Unnecessary Grapes
# Correct Pepper Onion
# Rearrange Grapes
# Correct Tomatoes Potatoes
# Go Shopping!
#
# Output2: Milk, Onion, Salt, Water, Banana

grocery_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split(" ")
    if command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in grocery_list:
            grocery_list[grocery_list.index(old_item)] = new_item
        command = input()
        continue

    if command[0] == "Urgent":
        if command[1] not in grocery_list:
            grocery_list.insert(0, command[1])

    elif command[0] == "Unnecessary":
        if command[1] in grocery_list:
            grocery_list.remove(command[1])

    elif command[0] == "Rearrange":
        if command[1] in grocery_list:
            grocery_list.remove(command[1])
            grocery_list.append(command[1])

    command = input()

print(*grocery_list, sep=", ")

# initial_list = input().split("!")
# info_data = input()
#
#
# while info_data != "Go Shopping!":
#
#     if "Correct" in info_data:
#         _, old_item, new_item = info_data.split()
#         if old_item in initial_list:
#             initial_list[initial_list.index(old_item)] = new_item
#         info_data = input()
#         continue
#
#     command, item = info_data.split()
#
#     if command == "Urgent":
#         if item not in initial_list:
#             initial_list.insert(0, item)
#
#     elif command == "Unnecessary":
#         if item in initial_list:
#             initial_list.remove(item)
#
#     elif command == "Rearrange":
#         if item in initial_list:
#             initial_list.remove(item)
#             initial_list.append(item)
#
#     info_data = input()
#
# print(*initial_list, sep=", ")