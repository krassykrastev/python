# def find_player_position(matrix, PLAYER):
#     for row in range(len(matrix)):
#         if PLAYER in matrix[row]:
#             return row, matrix[row].index(PLAYER)


def valid_move(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


initial_text = input()
size = int(input())

EMPTY_POSITION = '-'
PLAYER = 'P'

matrix = [[] * size for _ in range(size)]

# found the player's starting position, when creating the matrix

for ind in range(len(matrix)):
    matrix[ind] = list(input())
    if PLAYER in matrix[ind]:
        current_row, current_col = ind, matrix[ind].index(PLAYER)

n = int(input())

# player_starting_position = find_player_position(matrix, PLAYER)

# current_row, current_col = player_starting_position[0], player_starting_position[1]

for i in range(n):

    command = input()
    move = ()

    if command == 'up':
        move = (-1, 0)
    elif command == 'down':
        move = (1, 0)
    elif command == 'left':
        move = (0, -1)
    elif command == 'right':
        move = (0, 1)

    player_last_row, player_last_col = current_row, current_col
    current_row += move[0]
    current_col += move[1]

    if valid_move(current_row, current_col, size):
        current_position = matrix[current_row][current_col]
        if current_position != EMPTY_POSITION and current_position != PLAYER:
            matrix[player_last_row][player_last_col] = EMPTY_POSITION
            initial_text += current_position
            matrix[current_row][current_col] = PLAYER
        else:
            matrix[player_last_row][player_last_col] = EMPTY_POSITION
            matrix[current_row][current_col] = PLAYER

    else:
        initial_text = initial_text[:-1]
        current_row, current_col = player_last_row, player_last_col

print(f"{initial_text}")

for line in range(len(matrix)):
    print(f"{''.join(matrix[line])}")