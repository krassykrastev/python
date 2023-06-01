numbers = input().split(' ')
numbers_as_float = list(map(float, numbers))

print(list(map(round, numbers_as_float)))

# another solution
# numbers = [round(float(i)) for i in input().split()]
# print(numbers)