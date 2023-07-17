# You are a world traveler, and your next goal is to make a world tour.
# To do that, you have to plan out everything first.
# To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops.
# Until you receive the command "Travel", you will be given some commands to manipulate that initial string.
# The commands can be:
# •	"Add Stop:{index}:{string}":
#   o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
#   o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
#   o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
#
# Input1:
# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel
#
# Output1:
# Hawai::RomeCyprys-Greece
# Hawai::Rome-Greece
# Bulgaria::Rome-Greece
# Ready for world tour! Planned stops: Bulgaria::Rome-Greece
#
# Input2:
# Albania:Bulgaria:Cyprus:Deuchland
# Add Stop:3:Nigeria
# Remove Stop:4:8
# Switch:Albania: Azərbaycan
# Travel

string = input()

while True:
    line = input()

    if line == "Travel":
        break

    command_args = line.split(":")
    command = command_args[0]

    if command == "Add Stop":
        index = int(command_args[1])
        new_stop = command_args[2]

        if 0 <= index < len(string):
            string = string[:index] + new_stop + string[index:]

    elif command == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])

        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]

    elif command == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]

        string = string.replace(old_string, new_string)

    print(string)

print(f"Ready for world tour! Planned stops: {string}")