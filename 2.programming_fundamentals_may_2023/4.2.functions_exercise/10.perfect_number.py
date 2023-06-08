# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# • "We have a perfect number!" - if the number is perfect.
# • "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.
#
# Input1: 6
# Output1: We have a perfect number!
#
# Input2: 28
# Output2:We have a perfect number!
#
# Input3: 1236498
# Output3: It's not so perfect.

def is_perfect(some_number: int) -> str:
    divisors_sum= 0
    for divisor in range (1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return 'We have a perfect number!'
    return "It's not so perfect."
number = int(input())
print(is_perfect(number))