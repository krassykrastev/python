# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console.
# Use an appropriate name for the function.
#
# Input1:
# 2
# 5
# 3
#
# Output1: 2
#
# Input2:
# 600
# 342
# 123
#
# Output2: 123
#
# Input3:
# 25
# 21
# 4
#
# Output3: 4

def smallest_number(some_numbers):
    min_element = min(some_numbers)
    return min_element

first_number = int(input())
second_number = int(input())
third_number = int(input())

numbers = [first_number, second_number, third_number]
smallest_element = smallest_number(numbers)

print(smallest_element)