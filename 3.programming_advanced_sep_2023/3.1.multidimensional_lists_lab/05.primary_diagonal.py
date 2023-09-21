# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# On the first line, you will receive an integer N – the size of a square matrix. The next N lines hold the values for
# each column - N numbers, separated by a single space.
#
# Input1:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
#
# Output1:
# 4
#
# Input2:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
#
# Output2:
# 15

n = int(input())
matrix = []

for row in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

sum_diagonal = 0

for row_index in range(n):
    sum_diagonal += matrix[row_index][row_index]

print(sum_diagonal)
