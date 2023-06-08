# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints
# all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number
#
# Input1: 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
# Output1:
# Positive: 1, 0, 5, 3, 4, 12, 19
# Negative: -2, -100, -20, -33
# Even: -2, 0, 4, -100, -20, 12
# Odd: 1, 5, 3, 19, -33
#
# Input2: 1, 2, 53, 2, 21
# Output2:
# Positive: 1, 2, 53, 2, 21
# Negative:
# Even: 2, 2
# Odd: 1, 53, 21

numbers = input().split(', ')

positive = [number for number in numbers if int(number) >= 0]
negative = [number for number in numbers if int(number) < 0]
even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")