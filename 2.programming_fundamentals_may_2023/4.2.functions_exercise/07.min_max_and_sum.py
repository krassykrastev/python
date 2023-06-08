# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
# The output should be as follows:
# • On the first line: "The minimum number is {minimum number}"
# • On the second line: "The maximum number is {maximum number}"
# • On the third line: "The sum number is: {sum of all numbers}"
#
# Input1: 2 4 6
# Output1:
# The minimum number is 2
# The maximum number is 6
# The sum number is: 12
#
# Input2: 12 52 11 53 2 8 45
# Output2:
# The minimum number is 2
# The maximum number is 53
# The sum number is: 183

sum_of_numbers = 0
list_of_numbers_as_string = input().split(' ')
list_of_numbers_as_digits = list(map(int, list_of_numbers_as_string))

min_number = min(list_of_numbers_as_digits)
max_number = max(list_of_numbers_as_digits)

for number in list_of_numbers_as_string:
    sum_of_numbers += int(number)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_of_numbers}')