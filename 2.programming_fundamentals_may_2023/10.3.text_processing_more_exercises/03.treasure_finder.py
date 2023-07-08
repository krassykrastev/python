# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and
# its coordinates. On the first line, you will receive a key (sequence of numbers separated by a space).
# On the next few lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character with a corresponding number of the
# key sequence. You choose a key number from the sequence by just looping through it. If the length of the key sequence
# is less than the string sequence, you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates. The type will be between the symbol
# "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".
#
# Input1:
# 1 2 1 3
# ikegfp'jpne)bv=41P83X@
# ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
# find
#
# Output1:
# Found gold at 10N70W
# Found Silver at 32S43W

key_numbers = [int(x) for x in input().split()]

while True:
    string = input()

    if string == "find":
        break

    decrypted_message = ""
    treasure_type = ""
    key_index = 0

    for character in string:

        key = key_numbers[key_index]
        current_character_ord = ord(character)
        current_character = chr(current_character_ord - key)
        decrypted_message += current_character

        if key_index >= len(key_numbers) - 1:
            key_index = 0
        else:
            key_index += 1

    treasure_type_list = decrypted_message.split("&")
    treasure_type = treasure_type_list[1]
    treasure_coordinates_list = decrypted_message.split("<")
    treasure_coordinates = treasure_coordinates_list[1]
    treasure_coordinates = treasure_coordinates[:-1]

    print(f"Found {treasure_type} at {treasure_coordinates}")