counter = 0

number = int(input())
digit = int(input())

while number > 0:
    remainder = number % 2
    if remainder == digit:
        counter += 1
    number = number // 2
print(counter)