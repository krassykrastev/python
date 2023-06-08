# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.
#
# Input1:
# abc
# 3
#
# Output1: abcabcabc
#
# Input2:
# String
# 2
#
# Output2: StringString

repeat_string = lambda string, n: string * n

input_string = input()
number_of_repeating = int(input())

print(repeat_string(input_string, number_of_repeating))