# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with the biggest sum of its
# values. On the first line, you will get matrix sizes in the format "{rows}, {columns}".  On the next rows, you will
# get elements for each column, separated with a comma and a space ", ". You should print the found submatrix and the
# sum of its elements, as shown in the examples.
#
# Input1:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
#
# Output1:
# 9 8
# 7 9
# 33
#
# Input2:
# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
#
# Output2:
# 12 13
# 16 17
# 58

data = input().split(", ")
rows = int(data[0])
cols = int(data[1])
matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

max_sum = float('-inf')

for rox_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[rox_index][col_index]
        next_element = matrix[rox_index][col_index + 1]
        element_bottom = matrix[rox_index + 1][col_index]
        element_diagonal = matrix[rox_index + 1][col_index + 1]
        sum_elements = current_element + next_element + element_bottom + element_diagonal

        if max_sum < sum_elements:
            max_sum = sum_elements
            max_sum_sub_matrix = [
                [current_element, next_element],
                [element_bottom, element_diagonal]]

print(*max_sum_sub_matrix[0])
print(*max_sum_sub_matrix[1])
print(max_sum)
