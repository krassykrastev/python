# You will be given a number n representing the number of rows of the field.
# On the following n lines, you will receive each field row as a string with numbers separated by a space.
# Each number greater than zero represents a ship with health equal to the number value.
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}".
# Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1.
# If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.
#
# Input1:
# 3
# 1 0 0 1
# 2 0 0 0
# 0 3 0 1
# 0-0 1-0 2-1 2-1 2-1 1-1 2-1
#
# Output1: 2
#
# Input2:
# 5
# 1 0 5 0 1
# 6 3 9 0 0
# 7 9 4 3 2
# 1 0 0 4 9
# 5 6 0 3 5
# 0-1 0-2 0-2 0-2 0-2 0-2 3-0
#
# Output2: 2

n = int(input())

ships = []

for ship in range(n):
    the_ship = list(map(int, input().split()))
    ships.append(the_ship)

attacks = list(map(str, input().split()))

destroyed = 0

for attack in attacks:
    the_attack = attack.split("-")
    row = int(the_attack[0])
    col = int(the_attack[1])
    ships[row][col] -= 1
    if ships[row][col] == 0:
        destroyed += 1

print(destroyed)