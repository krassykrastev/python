# Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines,
# you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.
# Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". You
# should start searching from the top left. If there is no such symbol, print the message "{symbol} does not occur in the matrix".
#
# Input1:
# 3
# ABC
# DEF
# X!@
# !
#
# Output1:
# (2, 1)
#
# Input2:
# 4
# asdd
# xczc
# qwee
# qefw
# 4
#
# Output2:
# 4 does not occur in the matrix

rows = int(input())

matrix = []

for row in range(rows):
    elements = list(input())
    matrix.append(elements)

searched_element = input()

position = None

for row_index in range(rows):

    if position:
        break

    for col_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][col_index]
        if current_element == searched_element:
            position = (row_index, col_index)
            print(position)
            break

if not position:
    print(f"{searched_element} does not occur in the matrix")
