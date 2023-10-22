def find_squirrel_position():
    for row in range(size):
        if "s" in matrix[row]:
            return [row, matrix[row].index("s")]


def find_hazelnuts(current_position):
    number_of_hazelnut = 0

    for step in steps:
        row = current_position[0] + directions[step][0]
        col = current_position[1] + directions[step][1]

        if row not in range(size) or col not in range(size):
            return f"The squirrel is out of the field.\nHazelnuts collected: {number_of_hazelnut}"

        if matrix[row][col] == "t":
            return f"Unfortunately, the squirrel stepped on a trap...\nHazelnuts collected: {number_of_hazelnut}"

        if matrix[row][col] == "h":
            number_of_hazelnut += 1
            if number_of_hazelnut == 3:
                return f"Good job! You have collected all hazelnuts!\nHazelnuts collected: {number_of_hazelnut}"

        matrix[row][col] = "*"
        current_position = [row, col]

    return f"There are more hazelnuts to collect.\nHazelnuts collected: {number_of_hazelnut}"


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}

size = int(input())
steps = input().split(", ")
matrix = [list(input()) for _ in range(size)]
squirrel_position = find_squirrel_position()
print(find_hazelnuts(squirrel_position))