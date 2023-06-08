# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.
#
# Input1:
# 2
# 5
#
# Output1: [2, 4, 6, 8, 10]
#
# Input2:
# 1
# 10
#
# Output2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

factor = int(input())
count = int(input())
list_of_numbers = []

for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)

print(list_of_numbers)