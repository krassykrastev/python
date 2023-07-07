# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.
#
# Input1: aaaaabbbbbcdddeeeedssaa
# Output1: abcdedsa
#
# Input2: qqqwerqwecccwd
# Output2: qwerqwecwd

final_text = ""
last_character = ""

text = input()

for current_character in text:
    if current_character != last_character:
        final_text += current_character
        last_character = current_character

print(final_text)