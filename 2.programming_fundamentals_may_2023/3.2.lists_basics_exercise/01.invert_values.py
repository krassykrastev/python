# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.
#
# Input1: 1 2 -3 -3 5
# Output1: [-1, -2, 3, 3, -5]
#
# Input2: -4 0 2 57 -101
# Output2: [4, 0, -2, -57, 101]

list_of_numbers = input().split()
opposite_numbers = []

for element in list_of_numbers:
    current_number = -int(element)
    opposite_numbers.append(current_number)

print(opposite_numbers)