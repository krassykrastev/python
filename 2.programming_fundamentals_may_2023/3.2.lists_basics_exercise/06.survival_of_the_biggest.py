output_numbers = []
list_of_numbers_as_string = input().split(' ')
count_of_numbers_to_remove = int(input())

for numbers in list_of_numbers_as_string:
    output_numbers.append(int(numbers))

for i in range(count_of_numbers_to_remove):
    smallest_number = min(output_numbers)
    output_numbers.remove(smallest_number)

print(*output_numbers, sep = ', ')