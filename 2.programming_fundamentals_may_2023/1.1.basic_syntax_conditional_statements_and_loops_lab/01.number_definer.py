# Write a program that reads a floating-point number and:
# - prints "zero" if the number is zero
# - prints "positive" or "negative"
# - adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds 1 000 000
#
# Input1: 25
# Output1: positive
#
# Input2: 0.7
# Output2: small positive
#
# Input3: 435247392.921
# Output3: large positive
#
# Input4: -0.005
# Output4: small negative
#
# Input5: -103.21
# Output5: negative
#
# Input6: -358583355123.001
# Output6: large negative

num = float(input())

if num == 0:
    print('zero')
elif num > 0:
    if num < 1:
        print('small positive')
    elif num > 1000000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(num) < 1:
        print('small negative')
    elif abs(num) > 1000000:
        print('large negative')
    else:
        print('negative')
