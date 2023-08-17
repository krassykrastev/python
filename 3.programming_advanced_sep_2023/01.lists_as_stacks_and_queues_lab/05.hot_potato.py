# Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid.
# Every n
# th toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to
# the next kid. It continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by
# a single space. On the second line, you will receive the n
# th toss (integer) in which a child leaves the game.
# Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the only kid left
# in the format "Last is {kid}"
#
# Input1:
# Tracy Emily Daniel
# 2
#
# Output1:
# Removed Emily
# Removed Tracy
# Last is Daniel
#
# Input2:
# George Peter Michael William Thomas
# 10
#
# Output2:
# Removed Thomas
# Removed Peter
# Removed Michael
# Removed George
# Last is William
#
# Input3:
# George Peter Michael William Thomas
# 1
#
# Output3:
# Removed George
# Removed Peter
# Removed Michael
# Removed William
# Last is Thomas

from _collections import deque

name_of_players = input().split()
step_of_hot_potato = int(input())

players = deque(name_of_players)
counter = 0

while len(players) > 1:
    counter += 1
    current_name_of_player = players.popleft()

    if counter == step_of_hot_potato:
        print(f"Removed {current_name_of_player}")
        counter = 0

    else:
        players.append(current_name_of_player)

print(f"Last is {players[0]}")

# from _collections import deque
#
# name_of_players = input().split()
# step_of_hot_potato = int(input())
#
# players = deque(name_of_players)
#
# while len(players) > 1:
#     for i in range(step_of_hot_potato - 1):
#         players.append(players.popleft())
#
#     print(f"Removed {players.popleft()}")
#
# print(f"Last is {players.pop()}")
