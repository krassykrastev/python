# You will be given two strings. Transform the first string into the second one, letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
#
# Input1:
# bubble gum
# turtle hum
#
# Output1:
# tubble gum
# turble gum
# turtle gum
# turtle hum
#
# Input2:
# Kitty
# Doggy
#
# Output2:
# Ditty
# Dotty
# Dogty
# Doggy

first_string = input()
second_string = input()
last_printed_string = first_string

for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part
    if new_string == last_printed_string:
        continue

    print(new_string)
    last_printed_string = new_string
