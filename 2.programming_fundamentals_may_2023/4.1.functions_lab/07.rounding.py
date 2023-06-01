def rounding():
    list_of_numbers_as_float = list(map(float, list_of_numbers))
    return list(map(round, list_of_numbers_as_float))

list_of_numbers = input().split(' ')

print(rounding())