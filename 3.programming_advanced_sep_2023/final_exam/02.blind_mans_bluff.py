def find_start_position(matrix):
    for row in range(len(matrix)):
        if "B" in matrix[row]:
            return [row, matrix[row].index("B")]


def move(the_matrix, current_directions, current_position):
    touched_opponents = 0
    moves_counter = 0
    while True:
        command = input()
        if command == "Finish" or touched_opponents == 3:
            return f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves_counter}"

        current_row, current_col = current_position[0] + current_directions[command][0], \
                                   current_position[1] + current_directions[command][1]

        if current_row not in range(rows) or current_col not in range(cols):
            continue

        if the_matrix[current_row][current_col] == "O":
            continue

        moves_counter += 1

        if the_matrix[current_row][current_col] == "P":
            touched_opponents += 1
            the_matrix[current_row][current_col] = "-"

        current_position = [current_row, current_col]


OTHER_PLAYERS = 3
rows, cols = list(map(int, input().split()))

matrix = [input().split() for _ in range(rows)]
directions = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
start_position = find_start_position(matrix)

print(move(matrix, directions, start_position))