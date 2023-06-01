list_of_numbers = input().split(' ')
list_of_numbers_as_float = list(map(float, list_of_numbers))

print(list(map(round, list_of_numbers_as_float)))