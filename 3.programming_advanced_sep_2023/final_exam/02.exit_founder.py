players = [{"name": x, "rest": False} for x in input().split(", ")]
matrix = [input().split() for _ in range(6)]

while True:
    player = players.pop(0)
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    step_on = matrix[row][col]

    if player["rest"]:
        player["rest"] = False

    elif step_on == "E":
        print(f"{player['name']} found the Exit and wins the game!")
        break

    elif step_on == "T":
        print(f"{player['name']} is out of the game! The winner is {players[0]['name']}.")
        break

    elif step_on == "W":
        player['rest'] = True
        print(f"{player['name']} hits a wall and needs to rest.")

    players.append(player)








#
#
# MATRIX_SIZE = 6
#
# players = {x: {"rest": False} for x in input().split(", ")}
# matrix = [input().split() for _ in range(MATRIX_SIZE)]
#
#
# def find_exit(player):
#     print(f"{player[0]} found the Exit and wins the game!")
#     exit()
#
#
# def trap(player):
#     print(f"{player[0]} is out of the game! The winner is {player[1]}.")
#     exit()
#
#
# def wall(player):
#     players[player[0]]["rest"] = True
#     print(f"{player[0]} hits a wall and needs to rest.")
#
#
# commands = {"E": find_exit, "T": trap, "W": wall}
#
# player_one, player_two = list(players.keys())
# player_counter = 0
#
# while True:
#     input_row, input_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
#     player_counter += 1
#     if player_counter % 2 == 0:
#         player = (player_two, player_one)
#     else:
#         player = (player_one, player_two)
#     if players[player[0]]["rest"]:
#         players[player[0]]["rest"] = False
#         continue
#     player_steps_on = matrix[input_row][input_col]
#     if player_steps_on != ".":
#         commands[player_steps_on](player)

'''
Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)'''