# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# • The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# • The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."
#
# Input1:
# 2
# Here is a name @George| and an age #18*
# Another name @Billy| #35* is his age
#
# Output1:
# George is 18 years old.
# Billy is 35 years old.
#
# Input2:
# 3
# random name @lilly| random digits #5*age
# @Marry| with age #19*
# here Comes @Garry|he is #48* years old
#
# Output2:
# lilly is 5 years old.
# Marry is 19 years old.
# Garry is 48 years old.

name = age = ""

lines_of_string = int(input())

for line in range(lines_of_string):
    text_string = input()
    for character_index in range(len(text_string)):
        if text_string[character_index] == "@":
            for name_character in range(character_index + 1, len(text_string)):
                if text_string[name_character] == "|":
                    break
                name += text_string[name_character]

        if text_string[character_index] == "#":
            for age_character in range(character_index + 1, len(text_string)):
                if text_string[age_character] == "*":
                    break
                age += text_string[age_character]

    print(f"{name} is {age} years old.")
    name = age = ""

# another solution
# def get_name_and_age(sentence):
#     name_first_index = sentence.index("@") + 1
#     name_last_index = sentence.index("|")
#     age_first_index = sentence.index("#") + 1
#     age_last_index = sentence.index("*")
#     name = sentence[name_first_index:name_last_index]
#     age = sentence[age_first_index:age_last_index]
#     return name, age
#
#
# number_of_entries = int(input())
# for sentence in range(number_of_entries):
#     current_sentence = input()
#     current_name, current_age = get_name_and_age(current_sentence)
#     print(f"{current_name} is {current_age} years old.")