rows, cols = map(int, input().split())
matrix = [list(input()) for _ in range(rows)]


def find_position(rows, matrix, symbol):
    for row in range(rows):
        if symbol in matrix[row]:
            return [row, matrix[row].index(symbol)]


def delivery(matrix, rows, cols, starting_position, steps):
    current_position = starting_position

    while True:
        command = input()
        next_step = current_position[0] + steps[command][0], current_position[1] + steps[command][1]
        next_position = matrix[next_step[0]][next_step[1]] \
            if next_step[0] in range(rows) and next_step[1] in range(cols) else False

        if next_position == "*":
            continue

        if not next_position:
            matrix[starting_position[0]][starting_position[1]] = " "
            print("The delivery is late. Order is canceled.")
            return '\n'.join("".join(row) for row in matrix)

        current_position = next_step
        if matrix[current_position[0]][current_position[1]] == "A":
            matrix[current_position[0]][current_position[1]] = "P"
            print("Pizza is delivered on time! Next order...")
            return '\n'.join("".join(row) for row in matrix)

        if matrix[current_position[0]][current_position[1]] == "P":
            matrix[current_position[0]][current_position[1]] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
            continue

        if matrix[current_position[0]][current_position[1]] == "-":
            matrix[current_position[0]][current_position[1]] = "."


starting_position = find_position(rows, matrix, "B")

steps = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}

print(delivery(matrix, rows, cols, starting_position, steps))