# Write a program that prints the calculated logarithm of any given number
# Input1:
# 10
# natural
#
# Output1:
# 2.30
#
# Input2:
# 10
# 10
#
# Output2:
# 1.00

from math import log

number = int(input())
command = input()

if command == "natural":
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, int(command)):.2f}")
