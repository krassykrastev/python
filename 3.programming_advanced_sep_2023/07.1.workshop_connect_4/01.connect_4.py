# create a simple two-player "Connect Four" game

ROWS = 6
COLS = 7

direction_mapper = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
]


class FullColumnError(Exception):
    pass


def print_matrix(matrix):
    for row in matrix:
        print(row)


def is_valid_column_choice(selected_column_index):
    if 0 <= selected_column_index < COLS:
        return True
    return False


def place_player_number(column_index, matrix, player_number):
    for row_index in range(ROWS - 1, -1, -1):
        if matrix[row_index][column_index] == 0:
            matrix[row_index][column_index] = player_number
            return row_index, column_index
    else:
        raise FullColumnError


def is_valid_place(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        return True
    return False


def requested_direction_count(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row + row_movement * i
        col_index_to_check = current_col + col_movement * i

        if not is_valid_place(row_index_to_check, col_index_to_check):
            break

        if matrix[row_index_to_check][col_index_to_check] != player:
            break

        count += 1
    return count


def opposite_direction_count(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row - row_movement * i
        col_index_to_check = current_col - col_movement * i

        if not is_valid_place(row_index_to_check, col_index_to_check):
            break

        if matrix[row_index_to_check][col_index_to_check] != player:
            break

        count += 1
    return count


def is_winner(current_row, current_col, matrix, player):
    for row_movement, col_movement in direction_mapper:
        count_direction = requested_direction_count(current_row, current_col, row_movement, col_movement, matrix, player)
        count_opposite_direction = opposite_direction_count(current_row, current_col, row_movement, col_movement, matrix, player)

        if (count_direction + count_opposite_direction) >= 3:
            return True
    return False


matrix = [[0 for _ in range(COLS)]for _ in range(ROWS)]
print_matrix(matrix)

player = 1

while True:
    try:
        selected_column_number = int(input(f"Player {player}, please choose a column:"))
        selected_column_index = selected_column_number - 1

        if not is_valid_column_choice(selected_column_index):
            raise ValueError

        current_row, current_col = place_player_number(selected_column_index, matrix, player)

        if is_winner(current_row, current_col, matrix, player):
            print(f"Player {player} wins!")
            print_matrix(matrix)
            break

        print_matrix(matrix)

    except ValueError:
        print(f"Player {player}, please select number between 1 and {COLS}")
        continue

    except FullColumnError:
        print(f"Player {player}, column {selected_column_number} is full, please select another one")
        continue

    player += 1
    player = 2 if player % 2 == 0 else 1

