# Write a program that reads different floating-point numbers from the console.
# When it receives a number between 1 and 100 inclusive, the program should stop reading and should print
# "The number {number} is between 1 and 100".
#
# Input1:
# -3
# 0.9
# 44
#
# Output1: The number 44.0 is between 1 and 100
#
# Input2:
# 0.5
# 90
# -4
# 101
#
# Output2: The number 90.0 is between 1 and 100

while True:
    number = float(input())

    if 1 <= number <= 100:
        print (f'The number {number} is between 1 and 100')
        break
