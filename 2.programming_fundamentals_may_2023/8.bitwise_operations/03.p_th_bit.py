# Write a program that prints the bit at position p of the given integer.
# We use the standard counting: from right to left, starting from 0.

number = int(input())
position = int(input())

bit = (number >> position) & 1

print(bit)