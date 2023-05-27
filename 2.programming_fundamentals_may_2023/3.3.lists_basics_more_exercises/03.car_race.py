left_car_time = 0
right_car_time = 0

sequence_of_numbers = input().split(' ')

for i in range(int(len(sequence_of_numbers) // 2)):
    left_car_time += int(sequence_of_numbers[i])
    if sequence_of_numbers[i] == '0':
        left_car_time *= 0.8
    right_car_time += int(sequence_of_numbers[-i-1])
    if sequence_of_numbers[-i-1] == '0':
        right_car_time *= 0.8
if left_car_time < right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
else:
    print(f'The winner is right with total time: {right_car_time:.1f}')