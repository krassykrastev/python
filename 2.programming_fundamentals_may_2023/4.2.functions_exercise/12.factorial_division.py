# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.
#
# Input1:
# 5
# 2
#
# Output1: 60.00
#
# Input2:
# 6
# 2
#
# Output2: 360.00

def calculate_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number

first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_factorial(first_number)
second_number_factorial = calculate_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f'{result:.2f}')