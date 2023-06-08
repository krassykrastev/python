# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().
#
# Input1: 1 2 3 4
# Output1: [2, 4]
#
# Input2: 1 2 3 -1 -2 -3
# Output2: [2, -2]

def is_even(some_number):
    return some_number % 2 == 0

numbers_as_string = input().split(' ')
numbers_as_digits = []

for number in numbers_as_string:
    numbers_as_digits.append(int(number))

result = list(filter(is_even, numbers_as_digits))

print(result)

# solution with lambda
# numbers_as_string = input().split(' ')
# numbers_as_digits = []
#
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers_as_digits))
#
# print(result)