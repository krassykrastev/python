# Read two integer numbers and, after that, exchange their values. Print the variable values before and after the exchange
#
# Input1:
# 5
# 10
#
# Output1:
# Before:
# a = 5
# b = 10
# After:
# a = 10
# b = 5
#
# Input2:
# 10
# 20
#
# Output2:
# Before:
# a = 10
# b = 20
# After:
# a = 20
# b = 10

number_a = int(input())
number_b = int(input())

print('Before:')
print(f'a = {number_a}')
print(f'b = {number_b}')

number_a, number_b = number_b, number_a

print('After:')
print(f'a = {number_a}')
print(f'b = {number_b}')