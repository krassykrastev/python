# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its
# elements. There will be no case with two or more 3x3 squares with equal maximal sum.
#
# Input1:
# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
#
# Output1:
# Sum = 75
# 1 4 14
# 7 11 2
# 8 12 16
#
# Input2:
# 5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5
#
# Output2:
# Sum = 34
# 2 5 6
# 5 4 1
# 6 0 5

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {max_sum}")

max_submatrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]
