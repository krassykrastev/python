# You will be given an integer that represents a distance in meters.
# Write a program that converts meters to kilometers formatted to the second decimal point.
#
# Input1: 1852
# Output1: 1.85
#
# Input2: 798
# Output2: 0.80

meter = int(input())
kilometers = meter / 1000

print(f'{kilometers:.2f}')
