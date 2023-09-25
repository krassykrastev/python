# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
#
# Input1:
# 1 2 3 |4 5 6 |  7  88
# 7 | 4  5|1 0| 2 5 |3
# 1| 4 5 6 7  |  8 9
#
# Output1:
# 7 88 4 5 6 1 2 3
# 3 2 5 1 0 4 5 7
# 8 9 4 5 6 7 1
#
# Input2:
# 7 | 4  5|1 0| 2 5 |3
#
# Output2:
# 3 2 5 1 0 4 5 7
#
# Input3:
# 1| 4 5 6 7  |  8 9
#
# Output3:
# 8 9 4 5 6 7 1

strings = input().split("|")

matrix = []

for i in range(len(strings) - 1, -1, -1):
    row = [int(x) for x in strings[i].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, sep=" ", end=" ")
    