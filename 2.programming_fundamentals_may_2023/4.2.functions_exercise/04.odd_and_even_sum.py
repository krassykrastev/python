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