# Refactor the provided code, so you do not need to make any changes to it when you want to add new species to the animals' list
from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return 'Woof!'

class Cat(Animal):
    def make_sound(self):
        return 'Meow!'

def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
