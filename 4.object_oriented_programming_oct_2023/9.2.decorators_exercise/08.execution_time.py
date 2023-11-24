# Import the time module. Create a decorator called exec_time. It should calculate how much time a function needs to be
# executed. See the examples for more clarification.
#
# Test Code1:
# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
# print(loop(1, 10000000))
#
# Output1:
# 0.8342537879943848
#
# Test Code2:
# @exec_time
# def concatenate(strings):
#     result = ""
#     for string in strings:
#         result += string
#     return result
# print(concatenate(["a" for i in range(1000000)]))
#
# Output2:
# 0.14537858963012695
#
# Test Code3:
# @exec_time
# def loop():
#     count = 0
#     for i in range(1, 9999999):
#         count += 1
# print(loop())
#
# Output3:
# 0.4199554920196533

from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        return end - start
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())
