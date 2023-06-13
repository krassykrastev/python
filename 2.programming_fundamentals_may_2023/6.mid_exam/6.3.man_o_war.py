# The pirates encounter a huge Man-O-War at sea.
# Create a program that tracks the battle and either chooses a winner or prints a stalemate.
# On the first line, you will receive the status of the pirate ship, which is a string representing integer sections separated by ">".
# On the second line, you will receive the same type of status, but for the warship:
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
# The following lines represent commands until "Retire":
# •	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
# Check if the index is valid and if not, skip the command.
# If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."
# •	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive).
# Check if both indexes are valid and if not, skip the command.
# If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program: "You lost! The pirate ship has sunken."
# •	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health.
# Check if the index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.
# •	"Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections
# that are lower than 20% of the maximum health capacity. Print the following: "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"
# Input
# •	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# •	On the 2nd line, you are going to receive the status of the warship
# •	On the 3rd line, you will receive the maximum health a section of a ship can reach.
# •	On the following lines, until "Retire", you will be receiving commands.
# Output
# •	Print the output in the format described above.
# Constraints
# •	The section numbers will be integers in the range [1….1000]
# •	The indexes will be integers [-200….200]
# •	The damage will be an integer in the range [1….1000]
# •	The health will be an integer in the range [1….1000]
#
# Input1:
# 12>13>11>20>66
# 12>22>33>44>55>32>18
# 70
# Fire 2 11
# Fire 8 100
# Defend 3 6 11
# Defend 0 3 5
# Repair 1 33
# Status
# Retire
#
# Output1:
# 2 sections need repair.
# Pirate ship status: 135
# Warship status: 205
#
# Input2:
# 2>3>4>5>2
# 6>7>8>9>10>11
# 20
# Status
# Fire 2 3
# Defend 0 4 11
# Repair 3 18
# Retire
#
# Output2:
# 3 sections need repair.
# You lost! The pirate ship has sunken.

pirate_ship_status = [int(x) for x in input().split(">")]
war_ship_status = [int(x) for x in input().split(">")]
maximum_health_capacity = int(input())
command = input().split(" ")

while command[0] != "Retire":
    if command[0] == "Status":
        section_count = 0
        for section in pirate_ship_status:
            if section / maximum_health_capacity < 0.2:
                section_count += 1
        print(f"{section_count} sections need repair.")
        command = input().split(" ")
        continue

    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(war_ship_status):
            war_ship_status[index] -= damage
            if war_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for x in range(start_index, end_index + 1):
                pirate_ship_status[x] -= damage
                if pirate_ship_status[x] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship_status):
            if pirate_ship_status[index] + health > maximum_health_capacity:
                health = maximum_health_capacity - pirate_ship_status[index]
            pirate_ship_status[index] += health

    command = input().split(" ")

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(war_ship_status)}")