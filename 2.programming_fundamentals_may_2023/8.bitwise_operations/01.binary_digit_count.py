# You are given a positive integer number and one binary digit (0 or 1).
# Write a program that finds the number of binary digits in a given integer

counter = 0

number = int(input())
digit = int(input())

while number > 0:
    remainder = number % 2
    if remainder == digit:
        counter += 1
    number = number // 2
print(counter)