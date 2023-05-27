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