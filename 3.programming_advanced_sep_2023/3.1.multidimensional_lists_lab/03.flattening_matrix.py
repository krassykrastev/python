# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For
# example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4]. On the first line, you will receive
# the number of a matrix's rows. On the next rows, you will get the elements for each column separated with a comma and a space ", ".
#
# Input1:
# 2
# 1, 2, 3
# 4, 5, 6
#
# Output1:
# [1, 2, 3, 4, 5, 6]
#
# Input2:
# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
#
# Output2:
# [10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]

rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

flattened = []

for row in matrix:
    for el in row:
        flattened.append(el)

print(flattened)
