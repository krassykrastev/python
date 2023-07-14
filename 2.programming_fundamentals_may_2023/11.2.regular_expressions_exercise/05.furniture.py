# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a
# floating-point or integer number. You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"
#
# Input1:
# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
#
# Output1:
# Bought furniture:
# Sofa
# TV
# Total money spend: 2436.69

import re

command = input()
bought_furniture = []
total_money = 0

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"

while command != "Purchase":
    match = re.search(pattern, command)

    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)

    command = input()

print("Bought furniture:")

for furniture in bought_furniture:
    print(furniture)

print(f"Total money spend: {total_money:.2f}")
