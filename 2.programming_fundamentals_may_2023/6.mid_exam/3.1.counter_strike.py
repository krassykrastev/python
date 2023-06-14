# Write a program that keeps track of every won battle against an enemy. You will receive initial energy.
# Afterward, you will start receiving the distance you need to reach an enemy until the "End of battle" command is given, or you run out of energy.
# The energy you need for reaching an enemy is equal to the distance you receive.
# Each time you reach an enemy, you win a battle, and your energy is reduced.
# Otherwise, if you don't have enough energy to reach an enemy, end the program and print:
# "Not enough energy! Game ends with {count} won battles and {energy} energy".
# Every third won battle increases your energy with the value of your current count of won battles.
# Upon receiving the "End of battle" command, print the count of won battles in the following format:
# "Won battles: {count}. Energy left: {energy}"
# Input / Constraints
# •	On the first line, you will receive initial energy – an integer [1-10000].
# •	On the following lines, you will be receiving the distance of an enemy – an integer [1-10000]
#
# Input1:
# 100
# 10
# 10
# 10
# 1
# 2
# 3
# 73
# 10
#
# Output1: Not enough energy! Game ends with 7 won battles and 0 energy
#
# Input2:
# 200
# 54
# 14
# 28
# 13
# End of battle
#
# Output2: Won battles: 4. Energy left: 94

battles_won = 0

energy = int(input())
distance = input()

while distance != "End of battle":
    distance = int(distance)

    if energy >= distance and energy > 0:
        energy -= distance
        battles_won += 1

        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break

    distance = input()
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")