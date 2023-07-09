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

lines_of_string = int(input())

for line in range(lines_of_string):

    text_string = input()

    name = text_string[text_string.index("@") + 1:text_string.index("|")]

    age = text_string[text_string.index("#") + 1:text_string.index("*")]

    print(f"{name} is {age} years old.")
