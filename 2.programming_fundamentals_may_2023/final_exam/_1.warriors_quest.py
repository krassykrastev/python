# The city is overrun by demons. We need your help securing the civilians and defending our land. For the Alliance!
#
# First, you will receive a skill that needs the deciphered.
# Next, you will be receiving commands split by a single space until you get the "For Azeroth" command. There are 5 possible commands:
#
# •	"GladiatorStance"
#   o	Replace all letters with upper case and print the result.
# •	"DefensiveStance"
#   o	Replace all letters with lower case and print the result.
# •	"Dispel {index} {letter}"
#   o	Replace the letter at the index with the given one and print "Success!"
#   o	If the index is invalid, print: "Dispel too weak."
# •	"Target Change {substring} {second substring}"
#   o	Replace the first substring with the second and print the result.
# •	"Target Remove {substring}"
#   o	Remove the substring from the string and print the result.
#
# If the input command is not in the list, print "Command doesn't exist!"
# Input / Constraints
# 	On the 1st line you are going to receive the string.
# 	On the next lines, until you receive "For Azeroth", you will be receiving commands.
# 	All commands are case sensitive.
# Output
# 	Print the output of the commands in the format described above.

ciphered_skill = input()
command_line = input()

while command_line != "For Azeroth":
    command = command_line.split()[0]

    if command == "GladiatorStance":
        ciphered_skill = ciphered_skill.upper()
        print(ciphered_skill)
    elif command == "DefensiveStance":
        ciphered_skill = ciphered_skill.lower()
        print(ciphered_skill)
    elif command == "Dispel":
        index = int(command_line.split()[1])
        letter = command_line.split()[2]
        if 0 <= index <= len(ciphered_skill)-1:
            ciphered_skill = list(ciphered_skill)
            ciphered_skill[index] = letter
            ciphered_skill = ''.join(ciphered_skill)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command_line.split()[1] == "Change":
        substring1 = command_line.split()[2]
        substring2 = command_line.split()[3]
        ciphered_skill = ciphered_skill.replace(substring1, substring2)
        print(ciphered_skill)
    elif command_line.split()[1] == "Remove":
        substring = command_line.split()[2]
        ciphered_skill = ciphered_skill.replace(substring,'')
        print(ciphered_skill)
    else:
        print("Command doesn't exist!")
    command_line= input()

# skill = input()
#
# line = input()
# while not line == "For Azeroth":
#     data = line.split()
#     command = data[0]
#     if command == "GladiatorStance":
#         skill = skill.upper()
#         print(skill)
#     elif command == "DefensiveStance":
#         skill = skill.lower()
#         print(skill)
#     elif command == "Dispel":
#         index = int(data[1])
#         letter = data[2]
#         if index in range(0, len(skill) + 1):
#             skill = skill[:index] + letter + skill[index + 1:]
#             print("Success!")
#         else:
#             print("Dispel too weak")
#     elif command == "Target":
#         to_do = data[1]
#         if to_do == "Change":
#             substring = data[2]
#             second_substring = data[3]
#             skill = skill.replace(substring, second_substring)
#             print(skill)
#         elif to_do == "Remove":
#             substring = data[2]
#             skill = skill.replace(substring, "", 1)
#             print(skill)
#     else:
#         print("Command doesn't exist!")
#     line = input()