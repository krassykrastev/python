# Write a program that:
# Write a program that reads a string with N integers from the console, separated by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.
#
# Input1: 1 2 3 4 5
# Output1: 5 4 3 2 1
#
# Input2: 1
# Output2: 1

string = input().split()
stack = []

while string:
    current_character = string.pop()
    stack.append(current_character)

print(' '.join(stack))
