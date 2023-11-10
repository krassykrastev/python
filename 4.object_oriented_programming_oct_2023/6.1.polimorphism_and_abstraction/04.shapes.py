# Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter. Create classes Circle
# (receives radius upon initialization) and Rectangle (receives height and width upon initialization) that implement
# those methods (returning the result). The fields of Circle and Rectangle should be private.
#
# Test code1:
# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
#
# Output1:
# 78.53981633974483
# 31.41592653589793
#
# Test code2:
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())
#
# Output2:
# 200
# 60

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
