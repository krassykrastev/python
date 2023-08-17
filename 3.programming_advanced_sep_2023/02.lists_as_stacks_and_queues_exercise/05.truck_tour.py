# There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive).
# For each petrol pump, you will receive two pieces of information (separated by a single space):
# -	The amount of petrol the petrol pump will give you
# -	The distance from that petrol pump to the next petrol pump (kilometers)
# You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter of petrol
# per 1 kilometer, and its tank has infinite petrol capacity.
# In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given amount of petrol.
# Your task is to calculate the first petrol pump from where the truck will be able to complete the circle.
# You never miss filling its tank at a petrol pump.
# Input
# •	On the first line, you will receive the number of petrol pumps - N
# •	On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance between
# that petrol pump and the next petrol pump, separated by a single space
# Output
# •	An integer which will be the smallest index of a petrol pump from which you can start the tour
#
# Input1:
# 3
# 1 5
# 10 3
# 3 4
#
# Output1: 1
#
# Input2:
# 5
# 22 5
# 14 10
# 52 7
# 21 12
# 36 9
#
# Output2: 0

from collections import deque

petrol_pumps = deque()
number_of_pumps = int(input())

for i in range(number_of_pumps):
    petrol_pumps.append(input().split())

for index in range(len(petrol_pumps)):
    litters = 0
    for pump in petrol_pumps:
        litters += int(pump[0])
        litters -= int(pump[1])
        if litters < 0:
            petrol_pumps.append(petrol_pumps.popleft())
            break

    else:
        print(index)
        break
