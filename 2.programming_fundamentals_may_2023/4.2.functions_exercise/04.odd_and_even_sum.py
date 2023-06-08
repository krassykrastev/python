# You will receive a single number.
# You should write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.
#
# Input1: 1000435
# Output1: Odd sum = 9, Even sum = 4
#
# Input2: 3495892137259234
# Output2: Odd sum = 54, Even sum = 22

def odd_even_numbers(some_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_odd_digits, sum_of_even_digits

number = input()
odd_digits, even_digits = odd_even_numbers(number)
print(f'Odd sum = {odd_digits}, Even sum = {even_digits}')