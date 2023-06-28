# You are given an array of positive integers in a single line, separated by a space (' ').
# All numbers occur an even number of times except one number, which occurs an odd number of times.
# Find it using only bitwise operations.

result = 0

list_of_integers = [int(x) for x in input().split()]

for number in list_of_integers:
    result ^= number

print(result)