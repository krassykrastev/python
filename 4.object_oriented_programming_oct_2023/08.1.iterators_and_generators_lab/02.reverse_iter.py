# Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and
# __next__ methods, so the iterator returns the items of the iterable in reversed order.
#
# Test code:
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
#
# Output:
# 4
# 3
# 2
# 1

class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        self.index -= 1
        return self.iterable[self.index + 1]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
