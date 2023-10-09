# create a simple two-player "Tic-Tac-toe" game

def is_valid_sign(player_one_sign_):
    if player_one_sign_ in ['X', '0']:
        return True
    return False


def render_board(board_):
    for row_ in board_:
        print("| ", end="")
        print(" | ".join([sign if sign else " " for sign in row_]), end="")
        print(" |")


def is_row_win(board_):
    for row_ in board_:
        if len(set(row_)) == 1 and set(row_) != {None}:
            return True
    return False


def is_column_win(board_, current_sign_):
    for col_ in range(len(board_)):
        current_column = []
        for row_ in range(len(board_)):
            current_column.append(board_[row_][col_] == current_sign_)
        if all(current_column):
            return True
    return False


def is_diagonal_win(board_, current_sign_):
    diagonal_1, diagonal_2 = [], []
    for inx in range(len(board_)):
        diagonal_1.append(board_[inx][inx] == current_sign_)
        diagonal_2.append(board_[inx][len(board_) - 1 - inx] == current_sign_)
    return all(diagonal_1) or all(diagonal_2)


def is_win(board_, current_sign_):
    if any([is_row_win(board_), is_column_win(board_, current_sign_), is_diagonal_win(board_, current_sign_)]):
        return True
    return False


def is_row_win_possible(board_):
    if all(['X' in row_ and '0' in row_ for row_ in board_]):
        return False
    return True


def is_col_win_possible(board_):
    columns = []
    for col_ in range(len(board_)):
        current_column = []
        for row_ in range(len(board_)):
            current_column.append(board_[row_][col_])
        columns.append(current_column)
    if all(['X' in col_ and '0' in col_ for col_ in columns]):
        return False
    return True


def is_diagonal_win_possible(board_):
    diagonal_1, diagonal_2 = [], []
    for inx in range(len(board_)):
        diagonal_1.append(board_[inx][inx])
        diagonal_2.append(board_[inx][len(board_) - 1 - inx])
    if 'X' in diagonal_1 and '0' in diagonal_1 and 'X' in diagonal_2 and '0' in diagonal_2:
        return False
    return True


def is_draw(board_):
    if any([is_row_win_possible(board_), is_col_win_possible(board_), is_diagonal_win_possible(board_)]):
        return False
    return True


def is_valid_choice(board_, board_mapper_, choice_):
    if not choice_.isdigit():
        print("This is not a number")
        return False
    choice_ = int(choice_)

    if choice_ not in board_mapper_:
        print("Number out of range")
        return False

    if board_[board_mapper_[choice_][0]][board_mapper_[choice_][1]]:
        print("The position is already taken")
        return False
    return True


player_one = input("Player one name: ").strip()
player_two = input("Player two name: ").strip()

while True:
    player_one_sign = input(f"{player_one}, would you like to play with 'X' or '0'?").upper()
    if is_valid_sign(player_one_sign):
        break
    print("Please, enter 'X' or '0'")

player_two_sign = 'X' if player_one_sign == '0' else '0'

size = 3
board = [[None] * size for _ in range(size)]
board_mapper = {i + 1: (i // size, i % size) for i in range(size * size)}

print("This is the numeration of the board:")
[print(f"| {' | '.join([str(i + 1 + row * size) for i in range(size)])} |") for row in range(size)]
print(f"{player_one} starts first!")

turn = 1

while True:
    current_player = player_one if turn % 2 != 0 else player_two
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    while True:
        choice = input(f"{current_player} choose a free position [1-{size * size}]: ").strip()
        if is_valid_choice(board, board_mapper, choice):
            break

    row, col = board_mapper[int(choice)]
    board[row][col] = current_sign
    render_board(board)

    if is_win(board, current_sign):
        print(f"{current_player} won!")
        break

    if is_draw(board):
        print("Draw!")
        break

    turn += 1
