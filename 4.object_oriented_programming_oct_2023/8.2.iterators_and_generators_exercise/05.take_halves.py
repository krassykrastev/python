# You are given a skeleton with the following code:
# def solution():
#
#     def integers():
#         # TODO: Implement
#
#     def halves():
#
#         for i in integers():
#             # TODO: Implement
#
#     def take(n, seq):
#         # TODO: Implement
#
#     return (take, halves, integers)
#
# Implement the three generator functions:
# •	integers() - generates an infinite amount of integers (starting from 1)
# •	halves() - generates the halves of those integers (each integer / 2)
# •	take(n, seq) - takes the first n halves of those integers
#
# Test code1:
# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))
#
# Output1:
# [0.5, 1.0, 1.5, 2.0, 2.5]
#
# Test code2:
# take = solution()[0]
# halves = solution()[1]
# print(take(0, halves()))
#
# Output2:
# []

def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result
    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

print()

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
