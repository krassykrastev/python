# Write a program that translates messages from Morse code to English (capital letters).
# Use https://commons.wikimedia.org/wiki/File:International_Morse_Code.svg to help you (without the numbers).
# The words will be separated by a space (' '). Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.
#
# Input1: .. | -- .- -.. . | -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .
# Output1: I MADE YOU WRITE A LONG CODE
#
# Input2: .. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..
# Output2: I HOPE YOU ARE NOT MAD

decrypted_message = ""

morse_code_dictionary = {
    " ": "|",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

morse_code_string = input().split()

for morse_code_character in morse_code_string:
    for key in morse_code_dictionary:
        if morse_code_character == morse_code_dictionary[key]:
            decrypted_message += key

print(decrypted_message)