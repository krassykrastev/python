# You will receive three integer numbers.
# Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.
#
# Input1:
# 2
# 3
# -1
#
# Output1: negative
#
# Input2:
# 2
# 3
# 1
#
# Output2: positive

result = 'positive'
negative_digits_count = 0

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

if number_1 == 0 or number_2 == 0 or number_3 == 0:
    result = 'zero'
if number_1 < 0:
    negative_digits_count += 1
if number_2 < 0:
    negative_digits_count += 1
if number_3 < 0:
    negative_digits_count += 1
if negative_digits_count == 1 or negative_digits_count == 3:
    result = 'negative'

print(result)