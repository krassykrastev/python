import sys
number = int(input())
max_number = -sys.maxsize #-9223372036854775807
min_number = sys.maxsize #9223372036854775807

for num in range(number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
