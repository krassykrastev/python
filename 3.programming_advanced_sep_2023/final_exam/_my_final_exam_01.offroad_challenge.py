# John is quite an avid off-road fan. He bought a new jeep and made the necessary improvements to it. John is ready for
# new off-road adventures and can't wait to get started. In this challenge, he must save his fuel very carefully…
# There will be two sequences of integers. The first sequence will represent the initial fuel and the second -
# additional consumption index due to thin air at high altitudes, hence higher fuel consumption. There will also be a
# third sequence of integers, representing values equal to the necessary amount of fuel needed to reach the
# corresponding altitude in the challenge.
# Your task is to take the last fuel quantity from the fuel sequence and the first index from the additional consumption
# index sequence. Subtract the values and check the result.
# •	The corresponding altitude is reached if the calculated result is bigger or equal to the first element from the
# needed amount of fuel sequence. You need to remove both the fuel and the consumption index from their sequences as
# well as the needed amount of fuel index from their sequence.
# •	If the calculated result is smaller or not equal to the first element from the needed amount of fuel sequence, the
# corresponding altitude is not reached, movement cannot continue, and the program should end.
# Input
# •	The first line will represent the initial fuel – integers, separated by a single space.
# •	The second line will represent the consumption indexes that decrease initial fuel – integers, separated by a single space.
# •	The third line will represent the quantities needed to reach the corresponding altitude – integers, separated by a single space.
# Output
# •	On the first or the next n lines, output the corresponding message on the console from the following options:
# 	If John reaches the altitude, print the message:
#   o	"John has reached: Altitude 1"
#   o	…
#   o	"John has reached: Altitude {n}"
# 	If John fails to reach the altitude, print the message:
#   o	"John did not reach: Altitude {n}"
# •	On the next lines, based on whether he reached the top or not, print the following on the console in the specified format:
# 	If John doesn't have enough fuel to reach the top but has reached some altitude, display the following messages:
#   o	"John failed to reach the top.
# Reached altitudes: Altitude 1, … Altitude {n}"
# 	If John does not have enough fuel to reach the top and has not reached any altitude, print:
#   o	"John failed to reach the top.
# John didn't reach any altitude."
# 	If John manages to reach all the altitudes, he will reach the top. End the program and print on the console the following message:
#   o	"John has reached all the altitudes and managed to reach the top!"
#
# Input1:
# 200 90 40 100
# 20 40 30 50
# 50 60 80 90
#
# Output1:
# ohn has reached: Altitude 1
# John did not reach: Altitude 2
# John failed to reach the top.
# Reached altitudes: Altitude 1
#
# Input2:
# 40 66 123 100
# 10 30 70 33
# 40 55 77 100
#
# Output2:
# John has reached: Altitude 1
# John has reached: Altitude 2
# John did not reach: Altitude 3
# John failed to reach the top.
# Reached altitudes: Altitude 1, Altitude 2
#
# Input3:
# 199 190 100 100
# 20 40 30 50
# 50 60 70 80
#
# Output3:
# John has reached: Altitude 1
# John has reached: Altitude 2
# John has reached: Altitude 3
# John has reached: Altitude 4
# John has reached all the altitudes and managed to reach the top!
#
# Input4:
# 200 90 40 100
# 120 40 30 50
# 50 60 80 90
#
# Output4:
# John did not reach: Altitude 1
# John failed to reach the top.
# John didn't reach any altitude.

from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())
reached_altitudes = []
msg =""

for i in range(1, len(initial_fuel) + 1):
    last_fuel_quantity = initial_fuel[-1]
    additional_consumption = additional_consumption_index[0]

    result = last_fuel_quantity - additional_consumption
    fuel_needed = amount_of_fuel_needed[0]

    if result >= fuel_needed:
        initial_fuel.pop()
        additional_consumption_index.popleft()
        amount_of_fuel_needed.popleft()
        print(f"John has reached: Altitude {i}")
        reached_altitudes.append(f"Altitude {i}")

    else:
        if i == 1:
            msg = "John didn't reach any altitude."
            print(f"John did not reach: Altitude {i}")
            break
        else:
            print(f"John did not reach: Altitude {i}")
            msg =""
            break

if initial_fuel:
    print("John failed to reach the top.")
    if msg:
        print(msg)
        exit()

    print(f"Reached altitudes: ", end="")
    print(", ".join(reached_altitudes))

else:
    print("John has reached all the altitudes and managed to reach the top!")
