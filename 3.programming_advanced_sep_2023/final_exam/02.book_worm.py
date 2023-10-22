string = input()


def read_matrix():
    size_matrix = int(input())
    matrix = []
    for row in range(size_matrix):
        matrix.append(list(input()))
    return matrix


matrix = read_matrix()
player_position = []
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == "P":
            player_position.append(r)
            player_position.append(c)

row = player_position[0]
col = player_position[1]

commands_count = int(input())

for i in range(commands_count):
    matrix[row][col] = "-"
    command = input()
    previous_row = row
    previous_col = col

    if command == "up":
        row -= 1

    elif command == "down":
        row += 1

    elif command == "left":
        col -= 1

    elif command == "right":
        col += 1

    if row not in range(0, len(matrix)) or col not in range(0, len(matrix)):
        if string:
            string = string[:-1]
        row = previous_row
        col = previous_col
    else:
        if matrix[row][col].isalpha():
            string += matrix[row][col]

    matrix[row][col] = "P"


print(string)
print(*["".join(x) for x in matrix], sep="\n")