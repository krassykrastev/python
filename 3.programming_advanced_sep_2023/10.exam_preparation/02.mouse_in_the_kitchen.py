# A hungry little mouse is living in an old suburbs house. It walks around the kitchen cupboard every night and eats all
# the cheese. A lazy plump cat is guarding the kitchen, so the mouse should not walk out of the cupboard area.
# In the beginning, you will be given N and M – integers, separated by a comma - ",", indicating the cupboard’s area
# dimensions. On the next N lines, you will receive strings, representing the rows of the area, with M columns.
# After that, on each line, until the command "danger" appears as an input string, you will receive the possible
# directions for the mouse to move - "up", "down", "right", and "left".
# If the mouse steps outside the cupboard area, the cat will attack, and the cheese hunt is over. In that case, the
# program ends, keep the last known position of the mouse, before it steps outside the cupboard area and the following
# message is printed on the Console: "No more cheese for tonight!"
# Possible characters in the matrix are:
# •	M - represents the mouse's position.
# •	C – represents a piece of cheese.
# •	* – represents an empty position, nothing happens if the mouse steps on it.
# •	@ – represents a wall in the cupboard, cannot step on or go through it.
# •	T – represents a trap.
# The mouse starts from the M - position.
# •	If the mouse steps on the C – position, it eats the cheese from the field, and the position is marked with "*".
#  o	If this is the last cheese in the cupboard area, the mouse goes to sleep. Remember that this will be the last
#  known position of the mouse. The program ends and the following message is printed on the Console:
#  "Happy mouse! All the cheese is eaten, good night!"
# •	If the mouse steps into a trap (T -position), it will be trapped. Remember that this will be the last known position
# of the mouse. In that case, the program ends, and the following message is printed on the Console: "Mouse is trapped!"
# •	If the given direction leads the mouse towards the @ - position, this is a wall in the cupboard area.
# Do not make the move and skip the command.
# •	If the "danger" command is received before the mouse manages to eat all the cheese, the mouse disappears. Remember
# that this will be the last known position of the mouse and you will need it for the final state of the matrix. In that
# case, the program ends, and the following message is printed on the Console: "Mouse will come back later!"
# In the end, print the final state of the matrix (cupboard area) with the last known position of the mouse in it. Each row is on a new line.
# Input
# •	On the first line you will get the number of rows and columns of the matrix, separated by a comma.
# •	On the next N lines, you will receive strings, representing each row of the matrix.
# •	On each of the following lines, until the command "danger" appears as an input string, you will receive the possible
# directions for the mouse to move - "up", "down", "right", and "left".
# •	"danger" command – The mouse spots danger and disappears… for now!
# Output
# •	On the first line:
#   o	If the mouse steps outside the cupboard
# "No more cheese for tonight!"
#
#   o	If the mouse manages to eat all the cheese
# "Happy mouse! All the cheese is eaten, good night!"
#
#   o	If the mouse steps into a trap (T -position)
# "Mouse is trapped!"
#
#   o	If the "danger" command is received before the mouse manages to eat all the cheese –
# "Mouse will come back later!"
#
# •	On the next lines, print the final state of the matrix with the last known position of the mouse in it. Each row - on a new line, each row position with NO separator.
#
# Input1:
# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left
# down
# down
# down
# right
# danger
#
# Output1:
# Mouse is trapped!
# *****
# M@@**
# CC@**
# **@@*
# **CC*
#
# Input2:
# 4,8
# CC@**C*M
# T*@**CT*
# **@@@@**
# T***C***
# down
# right
# left
# down
# left
# danger
#
# Output2:
# No more cheese for tonight!
# CC@**C**
# T*@**CTM
# **@@@@**
# T***C***
#
# Input3:
# 6,3
# @CC
# @TC
# @C*
# @M*
# @**
# @**
# left
# up
# left
# right
# up
# up
# left
# left
# danger
#
# Output3:
# Happy mouse! All the cheese is eaten, good night!
# @M*
# @T*
# @**
# @**
# @**
# @**

ROWS_COUNT, COLS_COUNT = [int(el) for el in input().split(",")]


def is_in_area(row, col):
    if 0 <= row < ROWS_COUNT and 0 <= col < COLS_COUNT:
        return True
    else:
        return False


matrix = []
total_cheese_count = 0
mouse_position = None

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(ROWS_COUNT):
    row_data = list(input())
    if 'M' in row_data:
        col_index = row_data.index('M')
        mouse_position = [row_index, col_index]
    total_cheese_count += row_data.count("C")
    matrix.append(row_data)

direction = input()

eaten_cheese_count = 0

while direction != "danger":
    current_row, current_col = mouse_position
    row_to_go, col_to_go = direction_mapper[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if not is_in_area(desired_row, desired_col):
        print("No more cheese for tonight!")
        break

    elif matrix[desired_row][desired_col] == "C":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        eaten_cheese_count += 1
        mouse_position = [desired_row, desired_col]

        if eaten_cheese_count == total_cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[desired_row][desired_col] == "T":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        print("Mouse is trapped!")
        break

    elif matrix[desired_row][desired_col] == "@":
        direction = input()
        continue

    else:
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        mouse_position = [desired_row, desired_col]

    direction = input()

if direction == "danger":
    print("Mouse will come back later!")

for row in matrix:
    print(*row, sep="")
