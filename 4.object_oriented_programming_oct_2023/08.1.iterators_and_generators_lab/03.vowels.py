# Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods,
# so the iterator returns only the vowels from the string.
#
# Test code:
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
#
# Output:
# A
# e
# i
# u
# y
# o

class vowels:
    def __init__(self, text):
        self.text = text
        vowels_const = "aeiouyAEIOUY"
        self.found_vowels = [char for char in text if char in vowels_const]
        self.current_index = 0
        self.end_index = len(self.found_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index += 1
        return self.found_vowels[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
