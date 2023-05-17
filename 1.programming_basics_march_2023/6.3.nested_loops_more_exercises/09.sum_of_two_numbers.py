starting_interval = int(input())
final_interval = int(input())
magic_number = int(input())

combination_counter = 0
magic_number_condition = False
print_data = ''

for x in range(starting_interval, final_interval + 1):
    for y in range(starting_interval, final_interval + 1):

        combination_counter += 1
        if x + y == magic_number:
            magic_number_condition = True
            print_data = f'Combination N:{combination_counter} ({x} + {y} = {magic_number})'
            break
    if magic_number_condition:
        break

if magic_number_condition:
    print(print_data)
else:
    print(f'{combination_counter} combinations - neither equals {magic_number}')
