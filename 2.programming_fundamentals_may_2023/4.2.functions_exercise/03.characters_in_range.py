# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.
#
# Input1:
# a
# d
#
# Output1: b c
#
# Input2:
# #
# :
#
# Output2: $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
#
# Input3:
# #
# C
#
# Output3: $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B

def all_the_characters(first, second):
    characters = []
    for current_character_as_digit in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character_as_digit))
    return characters

first_character = input()
second_character = input()

result = all_the_characters(first_character, second_character)
print(' '.join (result))