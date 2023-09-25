# You are participating in a Firearm course. It is a training day at the shooting range. You will be given a matrix with
# 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with the symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move
# if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot
# only the nearest target. When you have shot a target, the field becomes an empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
# •	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
#
# Input1:
# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1
#
# Output1:
# Training not completed! 3 targets left.
# [4, 1]
#
# Input2:
# . . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right
#
# Output2:
# Training completed! All 2 targets hit.
# [4, 1]
# [2, 2]
#
# Input3:
# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left
#
# Output3:
# Training not completed! 1 targets left.
# [4, 1]

matrix = []
my_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, -0), 'down': (1, 0)}
targets_down = []

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "shoot":
        r = my_position[0] + directions[command[1]][0]
        c = my_position[1] + directions[command[1]][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets -= 1
                targets_down.append([r, c])
                break

            r += directions[command[1]][0]
            c += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == "move":
        steps = int(command[2])
        direction = command[1]

        r = my_position[0] + directions[command[1]][0] * steps
        c = my_position[1] + directions[command[1]][1] * steps

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for row in targets_down:
    print(row)
