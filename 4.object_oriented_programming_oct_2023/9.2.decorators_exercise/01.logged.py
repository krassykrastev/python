# Create a decorator called logged. It should return the name of the function that is being called and its parameters.
# It should also return the result of the execution of the function being called. See the examples for more clarification.
#
# Test Code1:
# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))
#
# Output1:
# you called func(4, 4, 4)
# it returned 6
#
# Test Code2:
# @logged
# def sum_func(a, b):
#     return a + b
# print(sum_func(1, 4))
#
# Output2:
# you called sum_func(1, 4)
# it returned 5

def logged(func):
    def wrapper(*args):
        result = func(*args)
        return f"you called {func.__name__}{args}\nit returned {result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

print()

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
