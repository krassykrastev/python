# Write a program that prints the sum of all found characters between two given characters (their ASCII code).
# On each of the first two lines, you will receive a single character. On the last line, you get a random string.
# Print the sum of the ASCII values of all characters in the random string between the two given characters in the ASCII table.
#
#
# Input1:
# .
# @
# dsg12gr5653feee5
#
# Output1: 363
#
# Input2:
# ?
# E
# @ABCEF
#
# Output2: 262

character_sum = 0

first_character = input()
first_character_ord = ord(first_character)
second_character = input()
second_character_ord = ord(second_character)
text_string = input()

for text_character in text_string:
    text_character_ord = ord(text_character)
    if first_character_ord > second_character_ord:
        if second_character_ord < text_character_ord < first_character_ord:
            character_sum += text_character_ord
    else:
        if first_character_ord < text_character_ord < second_character_ord:
            character_sum += text_character_ord

print(character_sum)