def find_mouse_position():
    for row in range(rows):
        if "M" in matrix[row]:
            return [row, matrix[row].index("M")]


rows, cols = list(map(int, input().split(",")))
matrix = [list(input()) for _ in range(rows)]
mouse_position = find_mouse_position()
directories = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
number_of_cheese = sum([row.count("C") for row in matrix])

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    current_row = mouse_position[0] + directories[command][0]
    current_col = mouse_position[1] + directories[command][1]

    if current_row not in range(rows) or current_col not in range(cols):
        print("No more cheese for tonight!")
        break

    if matrix[current_row][current_col] == "@":
        continue

    matrix[mouse_position[0]][mouse_position[1]] = "*"
    mouse_position = [current_row, current_col]

    if matrix[current_row][current_col] == "T":
        print("Mouse is trapped!")
        matrix[current_row][current_col] = "M"
        break

    if matrix[current_row][current_col] == "C":
        number_of_cheese -= 1
        if not number_of_cheese:
            matrix[current_row][current_col] = "M"
            print(f"Happy mouse! All the cheese is eaten, good night!")
            break

    matrix[current_row][current_col] = "M"

[print(''.join(x)) for x in matrix]