# Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the parameter
# passed to the decorated function is of the type given to the decorator. If it is, execute the function and return
# the result, otherwise return "Bad Type".
#
# Test Code1:
# @type_check(int)
# def times2(num):
#     return num*2
# print(times2(2))
# print(times2('Not A Number'))
#
# Output1:
# 4
# Bad Type
#
# Test Code2:
# @type_check(str)
# def first_letter(word):
#     return word[0]
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))
#
# Output2:
# H
# Bad Type

def type_check(type):
    def decorator(func):
        def wrapper(*args):
            if not isinstance(args[0], type):
                return "Bad Type"
            return func(*args)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))

print()


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
