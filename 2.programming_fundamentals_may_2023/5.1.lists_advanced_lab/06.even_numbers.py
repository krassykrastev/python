# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.
#
# Input1: 3, 2, 1, 5, 8
# Output1: [1, 4]
#
# Input2: 2, 4, 6, 9, 10
# Output2: [0, 1, 2, 4]

indices_of_even_numbers = []
list_of_numbers = list(map(int, input().split(', ')))
for index in range(len(list_of_numbers)):
    current_number = list_of_numbers[index]
    if current_number % 2 == 0:
        indices_of_even_numbers.append(index)

print(indices_of_even_numbers)

# another solution from SoftUni
# number_list = list(map(int, input().split(', ')))
# found_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))
# even_indices = list(filter(lambda a: a != 'no', found_indices_or_no))
# print(even_indices)