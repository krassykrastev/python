# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement
# the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given
# step. For more clarification, see the examples:
#
# Test code1:
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# Output1:
# 0
# 2
# 4
# 6
# 8
# 10
#
# Test code2:
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
#
# Output2:
# 0
# 10
# 20
# 30
# 40

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            i = self.i * self.step
            self.i += 1
            return i
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print()

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
