# Write a program that reads a matrix from the console and prints:
# •	The sum of all numbers in the matrix
# •	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will get
# elements for each column separated by a comma and a space ", ".
#
# Input1:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
#
# Output1:
# 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []
total_sum = 0

for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    total_sum += sum(elements)
    matrix.append(elements)

print(total_sum)
print(matrix)
