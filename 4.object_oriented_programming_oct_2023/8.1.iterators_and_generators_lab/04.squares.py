# Create a generator function called squares that should receive a number n.
# It should generate the squares of all numbers from 1 to n (inclusive).
#
# Test code:
# print(list(squares(5)))
#
# Output:
# [1, 4, 9, 16, 25]

def squares(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


print(list(squares(5)))

