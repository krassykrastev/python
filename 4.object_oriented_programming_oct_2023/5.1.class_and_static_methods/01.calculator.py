# Create a class called Calculator that has the following static methods:
# •	add(*args) - sums all the arguments passed to the function and returns the result
# •	multiply(*args) - multiplies all the numbers and returns the result
# •	divide(*args) - divides all the numbers (starting from the first one) and returns the result
# •	subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result
#
# Test code:
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
#
# Output:
# 19
# 30
# 50.0
# 70
from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
