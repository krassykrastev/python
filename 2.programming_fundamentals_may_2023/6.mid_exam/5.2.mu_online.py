# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
#   o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
#   o	First print: "You healed for {amount} hp."
#   o	After that, print your current health: "Current health: {health} hp."
# •	"chest"
#   o	You've found some bitcoins, the number in the second part.
#   o	Print: "You found {amount} bitcoins."
# •	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster.
# You should remove the monster's attack from your health.
#   o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
#   o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach: "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
# "You've made it!"
# "Bitcoins: {bitcoins}"
# "Health: {health}"
# Input / Constraints
# You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
# Output
# Print the corresponding messages described above.
#
# Input1: rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000
# Output1:
# You slayed rat.
# You slayed bat.
# You healed for 10 hp.
# Current health: 80 hp.
# You slayed rat.
# You found 100 bitcoins.
# You died! Killed by boss.
# Best room: 6
#
# Input2: cat 10|potion 30|orc 10|chest 10|snake 25|chest 110
# Output2:
# You slayed cat.
# You healed for 10 hp.
# Current health: 100 hp.
# You slayed orc.
# You found 10 bitcoins.
# You slayed snake.
# You found 110 bitcoins.
# You've made it!
# Bitcoins: 120
# Health: 65

initial_health = 100
bitcoins = 0
room = 0

dungeon_rooms = input().split("|")

for dungeon_room in dungeon_rooms:
    room_string = dungeon_room.split(" ")
    command = room_string[0]
    value = int(room_string[1])
    room += 1
    if command == "potion":
        if initial_health + value > 100:
            value = 100 - initial_health
        initial_health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        if initial_health - value <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            break
        else:
            initial_health -= value
            print(f"You slayed {command}.")

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")