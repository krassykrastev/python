# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value). On the
# first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for
# each column - N numbers separated by a single space. Print the absolute difference between the primary and the secondary diagonal sums.
#
# Input1:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
#
# Output1:
# 15
#
# Input2:
# 4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14
#
# Output2:
# 34

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [(matrix[i][i]) for i in range(n)]
secondary_diagonal = [(matrix[i][- i - 1]) for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

# n = int(input())
#
# matrix = []
#
# for row_index in range(n):
#     elements = [int(el) for el in input().split()]
#     matrix.append(elements)
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for i in range(n):
#     primary_diagonal.append(matrix[i][i])
#     secondary_diagonal.append(matrix[i][- i - 1])
#
# print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
