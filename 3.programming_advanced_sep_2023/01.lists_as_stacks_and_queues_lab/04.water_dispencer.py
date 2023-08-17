# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines,
# you will be given the names of some people who want to get water (each on a separate line) until you receive the
# command "Start". Add those people to a queue. Finally, you will receive some commands until the command
# "End":
# - "{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough
# water in the dispenser for that person.
# o If there is enough water, print "{person_name} got water" and remove him/her from the
# queue.
# o Otherwise, print "{person_name} must wait" and remove the person from the queue without
# reducing the water in the dispenser.
# - "refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".
#
# Input1:
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End
#
# Output1:
# Peter got water
# Amy got water
# 0 liters left
#
# Input2:
# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End
#
# Output2:
# Peter got water
# George got water
# Amy got water
# Alice must wait
# 2 liters left

from _collections import deque

people = deque()
water_amount = int(input())

while True:
    name = input()

    if name == "Start":
        break

    people.append(name)

while True:

    command = input().split()

    if command[0] == "refill":
        refill_litters = int(command[1])
        water_amount += refill_litters

    elif command[0] == "End":
        print(f"{water_amount} liters left")
        break

    else:
        person = people.popleft()
        litters_needed = int(command[0])

        if litters_needed <= water_amount:
            print(f"{person} got water")
            water_amount -= litters_needed

        else:
            print(f"{person} must wait")
