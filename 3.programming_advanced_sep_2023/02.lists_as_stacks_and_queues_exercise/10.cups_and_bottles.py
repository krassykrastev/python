# You will be given a sequence of integers – each indicating a cup's capacity (in litters). After that, you will be
# given another sequence of integers – each indicating a bottle's capacity (in litters). Your job is to try to fill up
# all the cups. You must start picking from the last received bottle and start filling from the first entered cup.
# You could pick exactly one bottle at a time. If the current bottle has N water, you give the first entered cup N water
# and reduce its integer value by N. When a cup's integer value reaches 0 or less, it gets removed. It is possible that
# the current cup's value is greater than the current bottle's value. In that case, you pick bottles until you reduce
# the cup's integer value to 0 or less. If a bottle's value is greater or equal to the cup's current value, you fill up
# the cup, and the remaining water becomes wasted. You should keep track of the wasted litters of water and print them
# at the end of the program. If you have managed to fill up all the cups, print the remaining water bottles, from the
# last entered – to the first. Otherwise, you must print the remaining cups ordered by the entrance –
# from the first entered – to the last.
# Input
# •	On the first line of input, you will receive the integers representing the cups' capacity, separated by a single space.
# •	On the second line of input, you will receive the integers representing the filled bottles, separated by a single space.
# Output
# •	On the first line:
#   o	If you filled all the cups, print the remaining bottles as specified:
# "Bottles: {bottle1} {bottle2} … {bottleN}"
#   o	If you used all the bottles of water, print the remaining cups as specified:
# "Cups: {cup1} {cup2} … {cupN}"
# •	On the second line, print the wasted litters of water in the following format:
# "Wasted litters of water: {wasted_litters_of_water}."
#
# Input1:
# 4 2 10 5
# 3 15 15 11 6
#
# Output1:
# Bottles: 3
# Wasted litters of water: 26
#
# Input2:
# 1 5 28 1 4
# 3 18 1 9 30 4 5
#
# Output2:
# Cups: 4
# Wasted litters of water: 35
#
# Input3:
# 10 20 30 40 50
# 20 11
#
# Output3:
# Cups: 30 40 50
# Wasted litters of water: 1

from collections import deque

cups_capacity = deque(map(int, input().split()))
bottles_capacity = deque(map(int, input().split()))

wasted_litters_of_water = 0

while cups_capacity and bottles_capacity:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_capacity.pop()

    if current_bottle >= current_cup:
        wasted_litters_of_water += current_bottle - current_cup
    else:
        cups_capacity.appendleft(current_cup - current_bottle)

if cups_capacity:
    print("Cups:", *cups_capacity, sep=" ")

elif bottles_capacity:
    print("Bottles:", *bottles_capacity, sep=" ")

print(f"Wasted litters of water: {wasted_litters_of_water}")
