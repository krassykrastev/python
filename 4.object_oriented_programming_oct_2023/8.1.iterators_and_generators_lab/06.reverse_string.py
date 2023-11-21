# Create a generator function called reverse_text that receives a string and
# yields all string characters on one line in reversed order.
#
# Test code:
# for char in reverse_text("step"):
#     print(char, end='')
#
# Output:
# pets
def reverse_text(text):
    current = len(text) - 1
    end = 0

    while current >= end:
        yield text[current]
        current -= 1


for char in reverse_text("step"):
    print(char, end='')
