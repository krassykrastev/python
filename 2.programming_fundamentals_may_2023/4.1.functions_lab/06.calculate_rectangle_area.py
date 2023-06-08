# Create a function that calculates and returns the area of a rectangle by given width and height.
# Print the result on the console.
#
# Input1:
# 3
# 4
#
# Output1: 12
#
# Input2:
# 6
# 2
#
# Output2: 12

def area_of_rectangle(some_width, some_height):
    return some_width * some_height

width = int(input())
height = int(input())

print(area_of_rectangle(width, height))