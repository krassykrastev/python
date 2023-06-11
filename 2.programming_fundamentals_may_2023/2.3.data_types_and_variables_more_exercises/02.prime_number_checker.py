# Write a program to check if a number is prime.
# A prime number is a natural number greater than 1, not a product of two smaller natural numbers.
# For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.
#
# Input1: 7
# Output1: True
# Input2: 8
# Output2: False
# Input3: 81
# Output3: False

is_prime = True
number = int(input())

if number > 2:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

print(is_prime)

# another solution from Stefi: Тони Троев ни каза за това математически доказано правило.
# При много големите прости числа цикъла ненужно ще върти много пъти. Ето защо може да върти само до корен квадратен от числото.
# from math import sqrt
# user_input = int(input())
# sqrt_to_input = int(sqrt(user_input))
# is_prime = True
# for i in range(2, sqrt_to_input + 1):
#     if user_input % i == 0:
#         is_prime = False
#         break
# print(is_prime)