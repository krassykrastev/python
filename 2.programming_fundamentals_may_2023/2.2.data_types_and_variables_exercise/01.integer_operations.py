# Write a program that reads four integer numbers.
# It should add the first to the second number, integer divide the sum by the third number, and multiply the result by the fourth number.
# Print the final result.
#
# Input1:
# 10
# 20
# 3
# 3
# Output1: 30
#
# Input2:
# 15
# 14
# 2
# 3
#
# Output2: 42

first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())

final_result = (first_number + second_number) // third_number * fourth_number

print(final_result)
