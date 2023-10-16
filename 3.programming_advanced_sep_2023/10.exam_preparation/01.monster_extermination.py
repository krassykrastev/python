# There will be given two sequences of integers.
# The first sequence represents the armor of the monsters. Each integer value represents the armor of a different monster.
# The second sequence represents the soldier's striking impact. Each integer value represents the strength of a strike performed by the soldier.
# Battle Rules:
# •	The monster at the front will be the first to face the soldier. Take the first armor value and the last strike
# strength value and compare the values.
# •	If the soldier's striking impact is greater than or equal to the monster's armor, the monster is killed, and its
# armor is removed from the sequence. The soldier's strike impact is then decreased by the value of the monster's armor.
# The remaining striking impact value is added to the next strike element in the sequence (if any) or is considered to
# be the last and only element. Zero values should not be pushed back to the sequence.
# •	If the soldier's striking impact is less than the monster's armor, the strike is performed, but the monster survives
# with reduced armor. The soldier's striking impact value is removed from the sequence, and the original strike value
# decreases the monster's armor value. The monster is then moved to the back of the sequence.
# •	The battle goes on until one of the sequences becomes empty.
# Your Task:
# Write a console application to simulate the battle as described above. Implement the battle logic using appropriate
# data structures to manage the soldier's striking impact and the monsters' armor values. The program should then
# display the appropriate outcome of the battle based on the rules.
# Input
# •	The first line will represent the armor values - integers, comma-separated values.
# •	The second line will represent the soldier's striking impact values - integers, comma-separated values.
# Output
# •	If all the monsters are killed, the program should print on the Console a success message:
#   o	"All monsters have been killed!"
# •	If the soldier's striking impact stack becomes empty, the program should print on the Console a message indicating
# that the soldier has been defeated:
#   o	"The soldier has been defeated."
# •	The program should print on the Console the total number of monsters killed by the soldier, on a new line:
#   o	"Total monsters killed: {killed_monsters}"
#
# Input1:
# 20,15,10
# 5,15,10,25
#
# Output1:
# All monsters have been killed!
# Total monsters killed: 3
#
# Input2:
# 30,25,40,35
# 15,20,10,30
#
# Output2:
# The soldier has been defeated.
# Total monsters killed: 1

from collections import deque

monster_armors = deque([int(el) for el in input().split(",")])
soldier_strikes = [int(el) for el in input().split(",")]

total_kills = 0

while monster_armors and soldier_strikes:
    current_monster_defence = monster_armors.popleft()
    current_solder_power = soldier_strikes.pop()

    if current_solder_power >= current_monster_defence:
        total_kills += 1
        current_solder_power -= current_monster_defence

        if not soldier_strikes and current_solder_power > 0:
            soldier_strikes.append(current_solder_power)
        elif soldier_strikes:
            soldier_strikes[-1] += current_solder_power

    else:
        current_monster_defence -= current_solder_power
        monster_armors.append(current_monster_defence)

if not monster_armors:
    print("All monsters have been killed!")

if not soldier_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {total_kills}")
