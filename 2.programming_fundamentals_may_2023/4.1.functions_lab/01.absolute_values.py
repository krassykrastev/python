# Write a program that receives a sequence of numbers, separated by a single space,
# and prints their absolute value as a list. Use abs().
#
# Input1: 1 2.5 -3 -4.5
# Output1: [1.0, 2.5, 3.0, 4.5]
#
# Input2: -0 1 10 -6.66
# Output2: [0.0, 1.0, 10.0, 6.66]

number_list = input().split(' ')

absolute_value = []

for num in number_list:
    absolute_value.append(abs(float(num)))

print(absolute_value)