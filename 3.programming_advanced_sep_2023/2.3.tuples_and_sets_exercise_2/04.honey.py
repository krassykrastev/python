# We think the process of making honey is amazing! Let's learn more about how bees make honey.
# Worker-bees collect nectar. When a worker-bee has found enough nectar, she returns to the hive to drop off the load
# and pass the nectar to waiting bees so they can really start the honey-making process. You will receive 3 sequences:
# •	a sequence of integers, representing working bees
# •	a sequence of integers, representing nectar
# •	a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
# Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the total honey
# waiting for bees made with the collected nectar. Step one: check if a bee has collected enough nectar. You should take
# the first bee and try to match it with the last nectar:
# •	If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the
# hive to drop off the load (step two).
# •	If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with
# the next nectar's value until the bee collects enough nectar.
# Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made.
# Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:
# "{matched_bee} {symbol} {matched_nectar}"
# The result represents the honey that is made from the passed nectar. The calculation should always return the absolute
# value of the result. After the calculation, remove the bee, the nectar, and the symbol.
# •	If the symbol is "/" and the nectar’s value is 0 (zero), skip the calculation and remove the bee, the nectar, and the symbol.
# Stop making honey when you are out of bees or nectar.
# Input
# •	On the first line, you will be given the values of bees - integers, separated by a single space
# •	On the second line, you will be given the nectar's values - integers, separated by a single space
# •	On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a single space
# Output
# •	On the first line - print the total honey made:
#   o	"Total honey made: {total honey}"
# •	On the next two lines print the bees or the nectar that are left, if there are any, otherwise skip the line:
#   o	"Bees left: {bee1}, {bee2}, … {beeN}"
#   o	"Nectar left: {nectar1}, {nectar2}, … {nectarN}"
#
# Input1:
# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
#
# Output1:
# Total honey made: 148
# Bees left: 99, 35, 0, 150
#
# Input2:
# 30
# 15 9 5 150 8
# * + + * -
#
# Output2:
# Total honey made: 4500
# Nectar left: 15, 9, 5

from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        symbol = symbols.popleft()
        collected_nectar = nectar.pop()
        bee = bees.popleft()
        if collected_nectar == 0:
            continue
        if symbol == "+":
            total_honey += abs(bee + collected_nectar)
        elif symbol == "-":
            total_honey += abs(bee - collected_nectar)
        elif symbol == "*":
            total_honey += abs(bee * collected_nectar)
        else:
            total_honey += abs(bee / collected_nectar)
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
