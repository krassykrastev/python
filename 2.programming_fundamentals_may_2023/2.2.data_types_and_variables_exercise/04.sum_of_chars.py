# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line, you will receive N – the number of lines.
# On the following N lines – you will receive a letter per line.
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].
#
# Input1:
# 5
# A
# b
# C
# d
# E
#
# Output1: The sum equals: 399
#
# Input2:
# 12
# S
# o
# f
# t
# U
# n
# i
# R
# u
# l
# z
# z
#
# Output2: The sum equals: 1263

number_of_characters = int(input())
total_sum = 0
for character in range(number_of_characters):
    current_character = input()
    total_sum += ord(current_character)
print(f'The sum equals: {total_sum}')