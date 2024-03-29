# Create a class called custom_range that receives a start (int) and an end (int) upon initialization.
# Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).
# Test code:
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start += 1
        return self.start - 1


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
