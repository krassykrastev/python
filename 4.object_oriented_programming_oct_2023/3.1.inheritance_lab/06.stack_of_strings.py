# Create a class Stack that can store only strings and has the following functionality:
# •	Instance attribute: data: list
# •	Method: push(element) – adds an element at the end of the stack
# •	Method: pop() – removes and returns the last element in the stack
# •	Method: top() - returns a reference to the topmost element of the stack
# •	Method: is_empty() - returns boolean True/False
# •	Override the string method to return the stack data in the format:
# "[{element(N)}, {element(N-1)} ... {element(0)}]"

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise ValueError("Element is not a string, please add onl strings")
        self.data.append(element)

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f'[{", ".join(reversed_data)}]'


stack = Stack()
print(stack.is_empty())
stack.push("asd")
print(stack.is_empty())
print(stack)
print(stack.top())
print(stack)
