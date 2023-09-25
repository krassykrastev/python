# Write a program that reads a matrix from the console and changes its values. On the first line, you will get the
# matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space. You
# will be receiving commands in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given
# indexes are in the range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.
#
# Input1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
#
# Output1:
# 6 2 3
# 4 3 6
# 7 8 9
#
# Input2:
# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
#
# Output2:
# Invalid coordinates
# Invalid coordinates
# -41 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 101

rows = int(input())
matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)
# matrix = [[int(x) for(x) in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")
        continue
    if command[0] == "Add":
        matrix[row][col] += value
    if command[0] == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")
