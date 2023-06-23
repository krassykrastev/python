# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message.
# After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations
# that need to be performed upon the concealed message to interpret it and reveal its true content.
# There are several types of instructions, split by '|'
# •	"Move {number of letters}":
#   o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
#   o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
#   o	Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"
#
# Input1:
# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode
#
# Output1: The decrypted message is: Hello
#
# Input2:
# owyouh
# Move|2
# Move|3
# Insert|3|are
# Insert|9|?
# Decode
#
# Output2: The decrypted message is: howareyou?

encrypted_message = input()

command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "ChangeAll":
        replace = command[1]
        replace_with = command[2]
        encrypted_message = encrypted_message.replace(replace, replace_with)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        first_part = encrypted_message[:index]
        second_part = encrypted_message[index:]
        encrypted_message = first_part + value + second_part
    elif command[0] == "Move":
        n_chars = int(command[1])
        chars_to_move = encrypted_message[:n_chars]
        first_part = encrypted_message[n_chars:]
        encrypted_message = first_part + chars_to_move

    command = input()

print(f"The decrypted message is: {encrypted_message}")

# main_string = input()
#
# command = input()
#
#
# def move_sting(number, string):
#     return string[number:] + string[:number]
#
#
# def insert_string(index, value, string):
#     return string[:index] + value + string[index:]
#
#
# def change_all(substring, replacement, string):
#     return string.replace(substring, replacement)
#
#
# while command != "Decode":
#     command_type, *info = [int(x) if x.isdigit() else x for x in command.split("|")]
#     if command_type == "Move":
#         number = info[0]
#         main_string = move_sting(number, main_string)
#     else:
#         index_or_substring, value_or_replacement = info
#         if command_type == "Insert":
#             main_string = insert_string(index_or_substring, value_or_replacement, main_string)
#         elif command_type == "ChangeAll":
#             main_string = change_all(index_or_substring, value_or_replacement, main_string)
#
#     command = input()
#
# print(f"The decrypted message is: {main_string}")