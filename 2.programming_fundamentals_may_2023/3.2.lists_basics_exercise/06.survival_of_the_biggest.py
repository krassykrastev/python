# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones,
# and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".
#
# Input1:
# 10 9 8 7 6 5
# 3
#
# Output1: 10, 9, 8
#
# Input2:
# 1 10 2 9 3 8
# 2
#
# Output2: 10, 9, 3, 8

output_numbers = []
list_of_numbers_as_string = input().split(' ')
count_of_numbers_to_remove = int(input())

for numbers in list_of_numbers_as_string:
    output_numbers.append(int(numbers))

for i in range(count_of_numbers_to_remove):
    smallest_number = min(output_numbers)
    output_numbers.remove(smallest_number)

print(*output_numbers, sep = ', ')