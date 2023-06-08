# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().
#
# Input1: 6 2 4
# Output1: [2, 4, 6]
#
# Input2: 12 52 11 53 2 8 45
# Output2: [2, 8, 11, 12, 45, 52, 53]

list_of_numbers = input().split(' ')
sorted_list_of_numbers = sorted(map(int, list_of_numbers))

print(sorted_list_of_numbers)