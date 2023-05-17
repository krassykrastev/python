import sys

n = int(input())

sum_numbers = 0
max_number = -sys.maxsize

for i in range(n):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

sum_numbers -= max_number

if sum_numbers == max_number:
    print('Yes')
    print(f'Sum = {sum_numbers}')
else:
    print('No')
    print(f'Diff = {abs(max_number - sum_numbers)}')
