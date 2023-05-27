number_a = int(input())
number_b = int(input())

print('Before:')
print(f'a = {number_a}')
print(f'b = {number_b}')

number_a, number_b = number_b, number_a

print('After:')
print(f'a = {number_a}')
print(f'b = {number_b}')