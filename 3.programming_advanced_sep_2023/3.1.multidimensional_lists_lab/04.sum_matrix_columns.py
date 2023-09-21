# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}". On the next rows, you will get
# elements for each column separated with a single space.
#
# Input1:
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
#
# Output1:
# 12
# 10
# 19
# 20
# 8
# 7
#
# Input2:
# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9
#
# Output2:
# 12
# 15
# 18

data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    sum_cols = 0
    for row_index in range(rows):
        sum_cols += matrix[row_index][col_index]
    print(sum_cols)
