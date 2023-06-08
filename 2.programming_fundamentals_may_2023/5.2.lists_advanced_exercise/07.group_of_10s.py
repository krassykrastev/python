# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers
# sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# • The numbers 2, 8, 4, and 10 fall into the group of 10's.
# • The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.
#
# Input1: 8, 12, 38, 3, 17, 19, 25, 35, 50
# Output1:
# Group of 10's: [8, 3]
# Group of 20's: [12, 17, 19]
# Group of 30's: [25]
# Group of 40's: [38, 35]
# Group of 50's: [50]
#
# Input2: 1, 3, 3, 4, 34, 35, 25, 21, 33
#
# Output2:
# Group of 10's: [1, 3, 3, 4]
# Group of 20's: []
# Group of 30's: [25, 21]
# Group of 40's: [34, 35, 33]

numbers = [int(s) for s in input().split(', ')]
current_group_of_numbers = 10

while numbers:
    filtered_numbers_for_current_group = []
    for current_number in numbers:
        if current_number <= current_group_of_numbers:
            filtered_numbers_for_current_group.append(current_number)
    print(f"Group of {current_group_of_numbers}'s: {filtered_numbers_for_current_group}")
    current_group_of_numbers += 10
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]