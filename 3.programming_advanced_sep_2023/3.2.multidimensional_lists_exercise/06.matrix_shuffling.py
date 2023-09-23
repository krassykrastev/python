# Write a program that reads a matrix from the console and performs certain operations with its elements. User input is
# provided similarly to the problems above - first, you read the dimensions and then the data. Your program should
# receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the
# coordinates of two points in the matrix. A valid command starts with the "swap" keyword along with four valid
# coordinates (no more, no less), separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus,
# you will be able to check if the operation was performed correctly).
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the
# given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value makes
# the coordinates not valid.
# Your program should finish when the command "END" is entered.
#
# Input1:
# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
#
# Output1:
# 5 2 3
# 4 1 6
# Invalid input!
# 5 4 3
# 2 1 6
#
# Input2:
# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
#
# Output2:
# Invalid input!
# World Hello
# Hello World

def are_coordinates_valid(r1,c1,r2,c2, rows, cols):
    return 0 <= r1 < rows and 0 <= r2 < rows and 0 <= c1 < cols and 0 <= c2 < cols

r, c = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(r)]

while True:
    line = input()
    if line == "END":
        break

    command = line.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if are_coordinates_valid(row1, col1, row2, col2, r, c):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
        