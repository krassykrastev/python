# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines,
# you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A".
# •	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she
# collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left"
# or "right". When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to
# continue collecting. Otherwise, if she steps into the rabbit hole or goes out of the territory, she can't return, and
# the program ends. In the end, the path she walked had to be marked with '*'. For more clarifications, see the examples below.
#
# Input1:
# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
#
# Output1:
# Alice didn't make it to the tea party.
# . * . . 1
# * * * . .
# 4 * . 1 .
# . . . 2 .
# . 3 . . .
#
# Input2:
# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
#
# Output2:
# She did it! She went to the party.
# * * . 1 1 . .
# * . . . 6 . 5
# * * . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2

n = int(input())
matrix = []
alice = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice = [row, col]

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
tea_bags = 0

while tea_bags < 10:
    command = input()
    move = possible_moves[command]
    row = alice[0] + move[0]
    col = alice[1] + move[1]

    if row < 0 or row >= n or col <0 or col >= n:
        break

    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break

    if matrix[row][col] not in '*.':
        tea_bags += int(matrix[row][col])

    matrix[row][col] = "*"
    alice = [row, col]

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=" ")
