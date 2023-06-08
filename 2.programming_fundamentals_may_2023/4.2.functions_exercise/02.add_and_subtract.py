# You will receive three integer numbers.
# Write functions named:
# • sum_numbers() that returns the sum of the first two integers
# • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.
#
# Input1:
# 23
# 6
# 10
#
# Output1: 19
#
# Input2:
# 1
# 17
# 30
#
# Output2: -12
#
# Input3:
# 42
# 58
# 100
#
# Output3: 0

def sum_numbers(first, second):
    return first + second
def subtract(sum, third):
    return sum - third
def add_and_subtract(number_one, number_two, number_three):
    sum_of_first_and_second_numbers = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_and_second_numbers, number_three)
    return result

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))