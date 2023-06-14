# As a young traveler, you gather items and craft new items.
# Input / Constraints
# You will receive a journal with some collecting items, separated with a comma and a space (", ").
# After that, until receiving "Craft!" you will be receiving different commands split by " - ":
# •	"Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this line.
# •	"Drop - {item}" - you should remove the item from your inventory if it exists.
# •	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
# •	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", ".
#
# Input1:
# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!
#
# Output1: Iron, Sword, Gold
#
# Input2:
# Iron, Sword
# Drop - Bronze
# Combine Items - Sword:Bow
# Renew - Iron
# Craft!
#
# Output2: Sword, Bow, Iron

collecting_items = input().split(", ")
command = input()

while command != "Craft!":
    current_command = command.split(" - ")
    if current_command[0] == "Collect":
        if current_command[1] not in collecting_items:
            collecting_items.append(current_command[1])
    elif current_command[0] == "Drop":
        if current_command[1] in collecting_items:
            collecting_items.remove(current_command[1])
    elif current_command[0] == "Combine Items":
        items = current_command[1].split(":")
        if items[0] in collecting_items:
            old_item_index = collecting_items.index(items[0])
            collecting_items.insert(old_item_index + 1, items[1])
    elif current_command[0] == "Renew":
        if current_command[1] in collecting_items:
            current_command[1] = collecting_items.pop(collecting_items.index(current_command[1]))
            collecting_items.append(current_command[1])
    command = input()

print(*collecting_items, sep=", ")