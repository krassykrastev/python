# You are a longtime captain of an old fishing vessel. The new fishing season begins and you prepare your ship to set
# sail in search of the big catch…
# You will be given an integer n for the size of the fishing area with a square shape. On the next n lines, you will
# receive the rows of the fishing area. You will be placed in a random position, marked with the letter 'S'. There will
# be fishing passages on random positions, marked with a single digit. There will be whirlpools marked with 'W'. All of
# the empty positions will be marked with '-'.
# Each turn until the "collect the nets" command is received you will be given commands for your movement. Move commands
# will be: "up", "down", "left", and "right".
# •	If you move to a fish passage, you collect the amount equal to the digit there, the passage disappears and should
# be replaced by '-'.
# •	If you fall into a whirlpool – the ship sinks and loses its catch, the program ends.
# •	If you leave the fishing area (go out of the boundaries of the matrix) depending on the move command you will be
# moved to the opposite side of the one you were on.
# /Example: In a 3x3 matrix you are at position [1,2] and receive the command "right" you will be moved to position [1,0]./
#  You need at least 20 tons of fish to be considered a successful season. Keep in mind that even if the quota is
#  reached the ship continues to move.
# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	The next n lines hold the values for every row.
# •	On each of the next lines, you will get a move command.
# Output
# •	On the first line:
# 	If the ship falls into a whirlpool, print only this message and stop the program:
#   o	"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [n,n]"
# 	If the ship reaches the quota:
#   o	"Success! You managed to reach the quota!"
# 	If the ship did not reach the quota:
#   o	"You didn't catch enough fish and didn't reach the quota!
# You need {lack of fish} tons of fish more."
# •	On the next lines.
# 	If the catch quantity is bigger than zero, print:
#   o	"Amount of fish caught: {quantity} tons."
# else: do not print anything.
# 	If you didn't get into a whirlpool, print the matrix.
#
# Input1:
# 4
# ---S
# ----
# 9-5-
# 34--
# down
# down
# right
# down
# collect the nets
#
# Output1:
# You didn't catch enough fish and didn't reach the quota! You need 8 tons of fish more.
# Amount of fish caught: 12 tons.
# ----
# ----
# --5-
# S4--
#
# Input2:
# 5
# S---9
# 777-1
# W333-
# 11111
# -----
# down
# down
# right
# down
# collect the nets
#
# Output2:
# You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [2,0]
#
# Input3:
# 5
# S---9
# 777-1
# --5--
# 11W11
# 988--
# down
# down
# down
# down
# down
# down
# right
# right
# right
# collect the nets
#
# Output3:
# Success! You managed to reach the quota!
# Amount of fish caught: 31 tons.
# ----9
# ---S1
# --5--
# -1W11
# -88--


def fishing_game():
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    position = None
    fish_caught = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'S':
                position = (i, j)

    while True:
        command = input()
        if command == "collect the nets":
            if fish_caught >= 20:
                print("Success! You managed to reach the quota!")
            else:
                print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_caught} tons of fish more.")
            break

        move_x, move_y = directions[command]
        new_x = (position[0] + move_x) % n
        new_y = (position[1] + move_y) % n


        if matrix[new_x][new_y].isdigit():
            fish_caught += int(matrix[new_x][new_y])
            matrix[new_x][new_y] = '-'
        elif matrix[new_x][new_y] == 'W':
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{new_x},{new_y}]")
            exit()

        matrix[position[0]][position[1]] = "-"
        position = (new_x, new_y)
        matrix[new_x][new_y] = "S"

    if fish_caught > 0:
        print(f"Amount of fish caught: {fish_caught} tons.")

    for row in matrix:
        print(''.join(row))


# Run the function
fishing_game()
