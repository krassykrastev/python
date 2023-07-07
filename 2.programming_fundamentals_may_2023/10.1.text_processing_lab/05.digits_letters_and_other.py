# Write a program that receives a single string. On the first line, print all the digits found in the string,
# on the second – all the letters, and on the third – all the other characters. There will always be at least one digit,
# one letter, and one other character.
#
# Input1: Agd#53Dfg^&4F53
#
# Output1:
# 53453
# AgdDfgF
# #^&

digits = letters = other_chars = ""

text_string = input()

for char in text_string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other_chars += char

print(digits)
print(letters)
print(other_chars)