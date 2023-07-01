# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
# Input1: text
# Output1:
# t -> 2
# e -> 1
# x -> 1
#
# Input2: text text text
# Output2:
# t -> 6
# e -> 3
# x -> 3

letters = {}

symbols = [char for char in input() if char != " "]

for symbol in symbols:
    if symbol in letters:
        letters[symbol] += 1
    else:
        letters[symbol] = 1

for key, value in letters.items():
    print(f"{key} -> {value}")