# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start with the last chocolate and try to match it with the first cup of milk. If their values are equal,
# you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the
# sequence and decrease the value of the chocolate by 5 without moving it from its position. If any of the values are
# equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to
# stop making chocolate milkshakes.
# Input
# •	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
# •	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
# •	On the first line, print:
#   o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
#   o	Otherwise: "Not enough milkshakes."
# •	On the second line - print:
#   o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
#   o	Otherwise: "Chocolate: empty"
# •	On the third line - print:
#   o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
#   o	Otherwise: "Milk: empty"
#
# Input1:
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
#
# Output1:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: 20
# Milk: 10, 55
#
# Input2:
# -10, -2, -30, 10
# -5
#
# Output2:
# Not enough milkshakes.
# Chocolate: -10, -2, -30, 10
# Milk: empty
#
# Input3:
# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
#
# Output3:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: empty
# Milk: 14, 6

from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    if chocolates[-1] <= 0 and milk_cups[0] <= 0:
        chocolates.pop()
        milk_cups.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    if chocolates[-1] == milk_cups[0]:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1
    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_cups) if milk_cups else 'empty'}")

