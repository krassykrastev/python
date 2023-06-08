# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers. Each number represents the time the car needs to pass through that step (the index).
# There will be two cars. The first one starts from the left side, and the other one starts from the right side.
# The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time).
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.
#
# Input1: 29 13 9 0 13 0 21 0 14 82 12
# Output1: The winner is left with total time: 53.8
#
# Input2: 123 20 4 0 13 0 0 5 5 14 0
# Output2: The winner is right with total time: 19.2

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