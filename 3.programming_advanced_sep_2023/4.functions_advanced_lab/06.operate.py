# Create a recursive function called recursive_power() which should receive a number and a power. Using recursion,
# return the result of number ** power. Submit only the function in the judge system.
#
# Input1:
# print(recursive_power(2, 10))
#
# Output1:
# 1024
#
# Input2:
# print(recursive_power(10, 100))
#
# Output2:
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
