# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible
# commands are "left", "right", "up" and "down". In the end, you will receive each row of the field on a separate line.
# The possible characters that may appear on the screen are:
# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively, moving with only one
# position in the given direction. If the miner has reached the edge of the field and the following command indicates
# that he has to get out of the area, he must remain in his current position and ignore the command. When the miner
# finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print
# whether the miner has succeeded in collecting the coal or not and his final position:
# •	If the miner has collected all coal in the field, the program stops, and you should print the message:
# "You collected all coal! ({row_index}, {col_index})".
# •	If the miner steps at "e", the game is over (the program stops), and you should print the message:
# "Game over! ({row_index}, {col_index})".
# •	If there are no more commands and none of the above cases had happened, you should print the message:
# "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
#
# Input1:
# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *
#
# Output1:
# Game over! (1, 3)
#
# Input2:
# 4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *
#
# Output2:
# You collected all coal! (2, 3)
#
# Input3:
# 6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *
#
# Output3:
# 3 pieces of coal left. (5, 0)

def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = int(input())
commands = input().split()

matrix = []
curr_row, curr_col = 0, 0
coal = 0
game_over = False


for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == "s":
            curr_row, curr_col = r, c
        elif matrix[r][c] == "c":
            coal += 1

for command in commands:
    if command == "up":
        if is_valid(curr_row - 1, curr_col, n):
            curr_row -= 1
    elif command == "down":
        if is_valid(curr_row + 1, curr_col, n):
            curr_row += 1
    elif command == "left":
        if is_valid(curr_row, curr_col - 1, n):
            curr_col -= 1
    elif command == "right":
        if is_valid(curr_row, curr_col + 1, n):
            curr_col += 1

    if matrix[curr_row][curr_col] == "e":
        print(f"Game over! ({curr_row}, {curr_col})")
        game_over = True
        break
    elif matrix[curr_row][curr_col] == "c":
        coal -= 1
        matrix[curr_row][curr_col] = "*"
        if coal == 0:
            print(f"You collected all coal! ({curr_row}, {curr_col})")
            game_over = True
            break

if not game_over:
    print(f"{coal} pieces of coal left. ({curr_row}, {curr_col})")
