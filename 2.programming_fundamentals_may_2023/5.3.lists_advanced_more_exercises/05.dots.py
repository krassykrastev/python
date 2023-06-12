# You will be given a number n representing the number of rows of a board of dots and dashes.
# On the following n lines, you will receive each row of the board as a string with symbols (dots and dashes only),
# separated by a single space.
# Your task is to find and print the largest count of dots that could be connected at once.
# You could only connect horizontally or vertically.
#
# Input1:
# 5
# . . - - -
# . . - - -
# - - - - -
# - - - . .
# - - - . .
#
# Output1: 4
#
# Input2:
# 6
# . . - . - .
# - . . . . .
# - . - - - -
# - . . - - -
# - . . . . -
# - - - . . -
#
# Output2: 18
#
# Input3:
# 4
# - . - . . –
# . - . . - .
# . - - - - -
# - - - . - -
#
# Output3: 4
# solution by ceo

def correct_lab_bounds(row, col):
    return row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0])

def check_wall(row, col):
    return lab[row][col] in "-–"

def check_already_visit(row, col):
    return lab[row][col] == "v"

def find_exit(row, col):
    return lab[row][col] == "."

def find_the_lab_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col) or check_already_visit(row, col):
        return

    path_steps.append(1)

    if find_exit(row, col):
        max_connected_points.append(sum(path_steps))

    lab[row][col] = "v"
    find_the_lab_path(row, col + 1, lab)  # check right
    find_the_lab_path(row, col - 1, lab)  # check left
    find_the_lab_path(row + 1, col, lab)  # check up
    find_the_lab_path(row - 1, col, lab)  # check down

row = int(input())
lab = []
max_connected_points = [0]
for _ in range(row):
    lab.append(list(input().split()))
col_range = len(lab[0])

for row in range(len(lab)):
    for col in range(col_range):
        path_steps = []
        if not check_wall(row, col):
            find_the_lab_path(row, col, lab)

print(max(max_connected_points))