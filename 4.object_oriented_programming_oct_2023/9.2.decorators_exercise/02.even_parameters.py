# Create a decorator function called even_parameters. It should check if all parameters passed to a function are even
# numbers and only then execute the function and return the result. Otherwise, don't execute the function and
# return "Please use only even numbers!"
#
# Test Code1:
# @even_parameters
# def add(a, b):
#     return a + b
#
# print(add(2, 4))
# print(add("Peter", 1))
#
# Output1:
# 6
# Please use only even numbers!
#
# Test Code2:
# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
#
# Output2:
# 384
# Please use only even numbers!

def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg % 2 != 0:
                return "Please use only even numbers!"
        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

print()

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
