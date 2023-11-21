# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two numbers
# in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number with
# the previous one.
#
# Test code1:
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
#
# Output1:
# 0
# 1
# 1
# 2
# 3
#
# Test code2:
# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
#
# Output2:
# 0

def fibonacci():
    curr_number = 0
    next_number = 1
    while True:
        yield curr_number
        curr_number, next_number = next_number, curr_number + next_number


generator = fibonacci()
for i in range(5):
    print(next(generator))

print()

generator = fibonacci()
for i in range(1):
    print(next(generator))
