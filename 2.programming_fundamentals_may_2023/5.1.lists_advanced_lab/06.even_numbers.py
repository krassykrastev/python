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