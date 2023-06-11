# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.
#
# Input1: 80
# Output1: 104.800
#
# Input2: 39
# Output2: 51.090

pound = int(input())
dollars = pound * 1.31

print(f'{dollars:.3f}')
