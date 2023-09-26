# The presents are ready, and Santa has to deliver them to the kids. You will receive an integer m for the number of
# presents Santa has and an integer n for the size of the neighborhood with a square shape. On the following lines, you
# will receive the matrix, which represents the neighborhood. Santa will be in a random cell, marked with the letter "S".
# Each cell stands for a house where children may live. If the cell has an "X" on it, that means there lives a naughty
# kid. Otherwise, if a nice kid lives there, the cell is marked with "V". There can also be cells marked with "C" for
# cookies. All of the empty positions will be marked with "-". Santa can move "up", "down", "left", and "right" with one
# position each time. These will be the commands that you receive. If he moves to a house with a nice kid, the kid
# receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a present. If the command sends
# Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all the kids around him*
# (meaning all of them will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the
# cell becomes "-". Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa
# doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
#
# Input1:
# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning
#
# Output1:
# - - - -
# - - - S
# - - - -
# X - - -
# Good job, Santa! 2 happy nice kid/s.
#
# Input2:
# 3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up
#
# Output2:
# Santa ran out of presents!
# - - - -
# V - - -
# - - S -
# - - - -
# No presents for 1 nice kid/s.


def get_next_position(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


presents = int(input())
size = int(input())
matrix = []

santa_row = 0
santa_col = 0
total_good_kids = 0
delivered_presents_to_good_kids = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 'V':
            total_good_kids += 1
        elif row_elements[col] == 'S':
            santa_row = row
            santa_col = col

while True:
    line = input()
    if line == "Christmas morning":
        break

    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = get_next_position(line, santa_row, santa_col)

    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        delivered_presents_to_good_kids += 1

    elif matrix[santa_row][santa_col] == 'C':
        if matrix[santa_row][santa_col - 1] == 'V' and presents:  #checking for good kid on the left
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row][santa_col - 1] = "-"
        elif matrix[santa_row][santa_col - 1] == 'X' and presents:   #checking for bad kid on the left
            presents -= 1
            matrix[santa_row][santa_col - 1] = "-"
        if matrix[santa_row][santa_col + 1] == 'V' and presents:    #checking for good kid on the right
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row][santa_col + 1] = "-"
        elif matrix[santa_row][santa_col + 1] == 'X' and presents:    #checking for bad kid on the right
            presents -= 1
            matrix[santa_row][santa_col + 1] = "-"
        if matrix[santa_row - 1][santa_col] == 'V' and presents:    #checking for good kid on upper row
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row - 1][santa_col] = "-"
        elif matrix[santa_row - 1][santa_col] == 'X' and presents:    #checking for bad kid on upper row
            presents -= 1
            matrix[santa_row - 1][santa_col] = "-"
        if matrix[santa_row + 1][santa_col] == 'V' and presents:    #checking for good kid on below row
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row + 1][santa_col] = "-"
        elif matrix[santa_row + 1][santa_col] == 'X' and presents:    #checking for bad kid on below row
            presents -= 1
            matrix[santa_row + 1][santa_col] = "-"

    matrix[santa_row][santa_col] = 'S'

    if presents == 0 or delivered_presents_to_good_kids == total_good_kids:
        break

if presents == 0 and delivered_presents_to_good_kids < total_good_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if delivered_presents_to_good_kids == total_good_kids:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")

else:
    print(f"No presents for {total_good_kids - delivered_presents_to_good_kids} nice kid/s.")
