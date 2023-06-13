# The pirates need to carry a treasure chest safely back to the ship, looting along the way.
# Create a program that manages the state of the treasure chest along the way.
# On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".
# "{loot1}|{loot2}|{loot3} … {lootn}"
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:
# •	"Loot {item1} {item2}…{itemn}":
# o	Pick up treasure loot along the way. Insert the items at the beginning of the chest.
# o	If an item is already contained, don't insert it.
# •	"Drop {index}":
# o	Remove the loot at the given position and add it at the end of the treasure chest.
# o	If the index is invalid, skip the command.
# •	"Steal {count}":
# o	Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are.
# o	Print the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"
# In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest
# formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."
# Input
# •	On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
# •	On the following lines, until "Yohoho!", you will be receiving commands.
# Output
# •	Print the output in the format described above.
# Constraints
# •	The loot items will be strings containing any ASCII code.
# •	The indexes will be integers in the range [-200…200]
# •	The count will be an integer in the range [1….100]
#
# Input1:
# Gold|Silver|Bronze|Medallion|Cup
# Loot Wood Gold Coins
# Loot Silver Pistol
# Drop 3
# Steal 3
# Yohoho!
#
# Output1:
# Medallion, Cup, Gold
# Average treasure gain: 5.40 pirate credits.
#
# Input2:
# Diamonds|Silver|Shotgun|Gold
# Loot Silver Medals Coal
# Drop -1
# Drop 1
# Steal 6
# Yohoho!
#
# Output2:
# Coal, Diamonds, Silver, Shotgun, Gold, Medals
# Failed treasure hunt.

initial_loot = input().split("|")

command = input().split(" ")

while command[0] != "Yohoho!":

    if command[0] == "Loot":
        for index in range(1, len(command)):
            if command[index] not in initial_loot:
                initial_loot.insert(0, command[index])

    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))

    elif command[0] == "Steal":
        count = int(command[1])
        stolen_items = initial_loot[-count:]
        initial_loot = initial_loot[:-count]
        print(*stolen_items, sep=", ")

    command = input().split(" ")

if initial_loot:
    average_treasure_gain = sum(len(x) for x in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")