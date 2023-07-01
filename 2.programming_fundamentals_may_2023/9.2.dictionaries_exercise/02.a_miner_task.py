# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
#
# Input1:
# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop
#
# Output1:
# Gold -> 155
# Silver -> 10
# Copper -> 17
#
# Input2:
# gold
# 155
# silver
# 10
# copper
# 17
# gold
# 15
# stop
#
# Output2:
# gold -> 170
# silver -> 10
# copper -> 17

resources = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())
    if current_resource in resources.keys():
        resources[current_resource] += current_quantity
    else:
        resources[current_resource] = current_quantity

for key, value in resources.items():
    print(f"{key} -> {value}")