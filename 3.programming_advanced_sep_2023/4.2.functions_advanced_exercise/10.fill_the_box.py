# Write a function called fill_the_box that receives a different number of arguments representing:
# •	the height of a box
# •	the length of a box
# •	the width of a box
# •	different numbers - each representing the quantity of cubes. Each cube has an exact size of 1 x 1 x 1
# •	a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
#
# Input1:
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
#
# Output1:
# There is free space in the box. You could put 13 more cubes.
#
# Input2:
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
#
# Output2:
# No more free space! You have 17 more cubes.
#
# Input3:
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
#
# Output3:
# There is free space in the box. You could put 960 more cubes.

def fill_the_box(*args):
    box_volume = args[0] * args[1] * args[2]
    cubes = 0
    for item in args[3:]:
        if item == "Finish":
            break
        cubes += item
    if box_volume > cubes:
        return f"There is free space in the box. You could put {box_volume - cubes} more cubes."
    return f"No more free space! You have {cubes - box_volume} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
