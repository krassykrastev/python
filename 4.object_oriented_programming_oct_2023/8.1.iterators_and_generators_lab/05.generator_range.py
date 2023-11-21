# Create a generator function called genrange that receives a start (int) and an end (int) upon initialization.
# It should generate all the numbers from the start to the end (inclusive).
#
# Test code:
# print(list(genrange(1, 10)))
#
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def genrange(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


print(list(genrange(1, 10)))
