# In a folder called project create two files: animal.py and dog.py:
# •	In the animal.py file, create a class called Animal with a single method eat() that returns: "eating…".
# •	In the dog.py file, create a class called Dog with a single method bark() that returns: "barking…".
# The Dog should inherit from Animal.

from project.dog import Dog

d = Dog()
print(d.bark())
print(d.eat())
