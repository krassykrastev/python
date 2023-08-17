# Create a program that checks if inputs are valid and decrypt it.
# On the first line you will receive a number that indicates how many inputs you will receive on the next lines.
#
# You will read lines with a boss name and title and you should check if they are valid, considering the following rules:
# 	Boss - the name should be in upper case letters, should be minimum four letters long and should be surrounded by "|"
# 	Title - contains exactly 2 words and they contain only alphabetical letters and 1 whitespace between them. The title should be surrounded by "#"
# 	The name and title should be split by a single ":"
# Example for a valid input:  |GEORGI|:#Lead architect#
# If the input is valid. Print in the following format:
# "{boss name}, The {title}
# >> Strength: {length of the name}
# >> Armour: {length of the title}"
#
# If the input is invalid, print "Access denied!"
# Input / Constraints
# 	On the 1st line, you will receive a number of inputs.
# 	On the next n lines, you will have to check if a boss has a valid name and title.
# Output
# 	Print the output with the format described above.
#
# Input1:
# 3
# |GEORGI|:#Lead architect#
# |Hristo|:#High Overseer#
# |STEFAN|:#Assistant Game Developer#
#
# Output1:
# GEORGI, The Lead architect
# >> Strength: 6
# >> Armour: 14
# Access denied!
# Access denied!
#
# Input2:
# 3
# |PETER|:#H1gh Overseer#
# |IVAN|:#Master detective#
# |KARL|: #Marketing lead#
#
# Output2:
# Access denied!
# IVAN, The Master detective
# >> Strength: 4
# >> Armour: 16
# Access denied!

import re
n = int(input())

for i in range(n):
    text = input()
    pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"
    match = re.match(pattern, text)

    if match is None:
        print("Access denied!")
        continue

    name = match[1]
    title = match[2]

    print(f'{name}, The {title}')
    print(f'>> Strength: {len(name)}')
    print(f'>> Armour: {len(title)}')

# import re
#
# count = int(input())
#
# regex = r"\|([A-Z]+)\|:#([A-Za-z]+ [A-Za-z]+)#"
#
# for _ in range(count):
#     current_input = input()
#     true_or_false = bool(re.match(regex, current_input))
#
#     if true_or_false:
#         data = re.findall(regex, current_input)
#         name = data[0][0]
#         title = data[0][1]
#
#         print(f"{name}, The {title}")
#         print(f">> Strength: {len(name)}")
#         print(f">> Armor: {len(title)}")
#
#     else:
#         print("Access denied!")

# import re
#
# count = int(input())
# pattern = r"(^\|([A-Z]{4,})\|)\:(#([A-Za-z]+\s[A-Za-z]+)#)"
# for validations in range(count):
#     current_boss = input()
#     valid_match = re.search(pattern, current_boss)
#     if valid_match:
#         name = valid_match.groups()[1]
#         title = valid_match.groups()[3]
#         strength = len(name)
#         armor = len(title)
#         print(f"{name}, The {title}")
#         print(f">> Strength: {strength}")
#         print(f">> Armor: {armor}")
#     else:
#         print("Access denied!")


################################################   Task Description   ################################################
# 2. Boss Rush