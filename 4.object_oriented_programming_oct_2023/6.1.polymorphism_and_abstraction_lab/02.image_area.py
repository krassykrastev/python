# Create a class called ImageArea which will store the width and the height of an image. Create a method called
# get_area() which will return the area of the image. We have also to implement all the magic methods for the comparison
# of two image areas (>, >=, <, <=, ==, !=), which will compare their areas.
#
# Test code1:
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)
#
# Output1:
# True
# True
#
# Test code2:
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3)
#
# Output2:
# False
# False
#
# Test code3:
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 <= a2)
# print(a1 < a3)
#
# Output3:
# True
# True

class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3)
#
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 <= a2)
# print(a1 < a3)
