# Write a program that prints the bit at position 1 of the given integer.
# We use the standard counting: from right to left, starting from 0.

position = 1
number = int(input())

bit = (number >> position) & 1

print(bit)