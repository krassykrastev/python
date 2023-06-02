def sum_numbers(first, second):
    return first + second
def subtract(sum, third):
    return sum - third
def add_and_subtract(number_one, number_two, number_three):
    sum_of_first_and_second_numbers = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_and_second_numbers, number_three)
    return result

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))