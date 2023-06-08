# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# • even
# • odd
# • negative
# • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
#
# Input1:
# 5
# 33
# 19
# -2
# 18
# 998
# even
#
# Output1: [-2, 18, 998]
#
# Input2:
# 3
# 111
# -4
# 0
# negative
#
# Output2: [-4]

n = int(input())

numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()
filtered_numbers = []

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)

elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)
elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)
elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)

# alternative solution
# n = int(input())
# COMMAND_EVEN = 'even'
# COMMAND_ODD = 'odd'
# COMMAND_NEGATIVE = 'negative'
# COMMAND_POSITIVE = 'positive'
#
# numbers = [int(input()) for i in range(n)]
#
# filtered_numbers = []
#
# command = input()
#
# for num in numbers:
#     filter_command = (
#         (command == COMMAND_EVEN and num % 2 == 0) or
#         (command == COMMAND_ODD and num % 2 != 0) or
#         (command == COMMAND_POSITIVE and num >= 0) or
#         (command == COMMAND_NEGATIVE and num < 0)
#         )
#
#     if filter_command:
#         filtered_numbers.append(num)
#
# print(filtered_numbers)
