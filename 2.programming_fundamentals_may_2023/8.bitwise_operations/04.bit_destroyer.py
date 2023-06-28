# Write a program that sets the bit at position p to 0. Print the resulting integer.

number = int(input())
position = int(input())

mask = ~(1 << position)
result = number & mask

print(result)