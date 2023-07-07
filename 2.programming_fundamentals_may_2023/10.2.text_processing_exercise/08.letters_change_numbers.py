# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters. For the given string, you should perform different
# mathematical operations to achieve a result:
# • First, if the letter in front of the number is:
# o Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# • Next, if the letter after the number is:
# o Uppercase: subtract its position from the resulting number (starting from 1)
# o Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping
# track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers, it
# became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each string.
# Input
# • The input comes from the console as a single line, holding a sequence of strings
# • Strings are separated by one or more white spaces
# • The input data will always be valid. There is no need to check it explicitly
# Output
# • Print at the console a single number:
#   o The total sum of all processed numbers, formatted to the second decimal separator
#
# Input1: A12b s17G
# Output1: 330.00
#
# Input2: P34562Z q2576f H456z
# Output2: 46015.12
#
# Input3: a1A
# Output3: 0.00

total_sum = 0

all_the_strings = input().split()

for current_string in all_the_strings:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    current_number = int(current_string[1:len(current_string) - 1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_number / first_letter_position

    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += current_number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position

    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position

print(f"{total_sum:.2f}")