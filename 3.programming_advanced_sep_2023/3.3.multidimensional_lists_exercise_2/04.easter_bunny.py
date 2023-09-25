# Your task is to collect as many eggs as possible. On the first line, you will be given a number representing the size
# of the field. In the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking
# some of the directions, you should not consider the fields after the trap in this direction. The bunny can move within
# the field and cannot go outside its boundaries. Do not consider negative indices as valid ones. For more
# clarifications, see the examples below. Note: In some directions, the collected eggs can happen to be zero or a negative number.
#
# Input1:
# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
#
# Output1:
# right
# [3, 1]
# [3, 2]
# [3, 3]
# [3, 4]
# 87
#
# Input2:
# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
#
# Output2:
# down
# [6, 2]
# [7, 2]
# 113

n = int(input())

matrix = []
bunny = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs = float('-inf')
max_direction = ""
max_eggs_matrix = []

for direction, move in possible_moves.items():
    eggs = 0
    curr_eggs_matrix = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        curr_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and curr_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = curr_eggs_matrix

print(max_direction)
for row in max_eggs_matrix:
    print(row)
# [print(row) for row in max_eggs_matrix]
print(max_eggs)
