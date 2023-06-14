# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets.
# On the first line, you will receive a sequence of targets with their integer values, split by a single space.
# Then, you will start receiving commands for manipulating the targets until the "End" command. The commands are the following:
# •	"Shoot {index} {power}"
#   o	Shoot the target at the index if it exists by reducing its value by the given power (integer value).
#   o	Remove the target if it is shot. A target is considered shot when its value reaches 0.
# •	"Add {index} {value}"
#   o	Insert a target with the received value at the received index if it exists.
#   o	If not, print: "Invalid placement!"
# •	"Strike {index} {radius}"
#   o	Remove the target at the given index and the ones before and after it depending on the radius.
#   o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
#  Example:  "Strike 2 2"
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# •	"End"
#   o	Print the sequence with targets in the following format and end the program: "{target1}|{target2}…|{targetn}"
# Input / Constraints
# •	On the first line, you will receive the sequence of targets – integer values [1-10000].
# •	On the following lines, until the "End" will be receiving the command described above – strings.
# •	There will never be a case when the "Strike" command would empty the whole sequence.
#
# Input1:
# 52 74 23 44 96 110
# Shoot 5 10
# Shoot 1 80
# Strike 2 1
# Add 22 3
# End
#
# Output1:
# Invalid placement!
# 52|100
#
# Input2:
# 1 2 3 4 5
# Strike 0 1
# End
#
# Output2:
# Strike missed!
# 1|2|3|4|5

def shoot(list_of_targets, target_index, shoot_power):
    if target_index in range(len(list_of_targets)):
        if list_of_targets[target_index] <= shoot_power:
            list_of_targets.pop(target_index)
        else:
            list_of_targets[target_index] -= shoot_power
    return list_of_targets

def add(list_of_targets, target_index, target_value):
    if target_index in range(len(list_of_targets)):
        list_of_targets.insert(target_index, target_value)
    else:
        print("Invalid placement!")
    return list_of_targets

def strike(list_of_targets, target_index, radius):
    if target_index - radius in range(len(list_of_targets)) and target_index + radius in range(len(list_of_targets)):
        list_of_targets = list_of_targets[0:target_index - radius] + list_of_targets[target_index + radius + 1:]
    else:
        print("Strike missed!")
    return list_of_targets

targets = [int(target) for target in input().split()]
command = input()

while command != "End":
    command = command.split()
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)

    command = input()

print(*targets, sep="|")

# targets = [int(x) for x in input().split()]
# data_info = input()
#
# while data_info != "End":
#     command, index, value = [int(x) if x[-1].isdigit() else x for x in data_info.split()]
#     valid_index = True
#     if not 0 <= index < len(targets):
#         valid_index = False
#
#     elif command == "Shoot":
#         targets[index] -= value
#         if targets[index] <= 0:
#             del targets[index]
#
#     if command == "Add":
#         if valid_index:
#             targets.insert(index, value)
#         else:
#             print("Invalid placement!")
#
#     elif command == "Strike" and valid_index:
#         start_radius = index - value
#         end_radius = index + value + 1
#         if 0 <= start_radius < end_radius < len(targets):
#             del targets[start_radius:end_radius]
#         else:
#             print("Strike missed!")
#     data_info = input()
#
# print(*targets, sep="|")