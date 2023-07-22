# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic.
# You want to play it all day long! So cancel all other arrangements and create your party!
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for
# your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by
# a single space in the following format:
# "{hero name} {HP} {MP}"
# -	HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game.
# You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
#   o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
#   o	"{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
#   o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
#   o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
# •	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200.
# (the MP can't go over the maximum value).
# •	 Print the following message:
#   o	"{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100),
# HP is increased to 100 (the HP can't go over the maximum value).
# •	 Print the following message:
#   o	"{hero name} healed for {amount recovered} HP!"
#
# Input1:
# 2
# Solmyr 85 120
# Kyrre 99 50
# Heal - Solmyr - 10
# Recharge - Solmyr - 50
# TakeDamage - Kyrre - 66 - Orc
# CastSpell - Kyrre - 15 - ViewEarth
# End
#
# Output1:
# Solmyr healed for 10 HP!
# Solmyr recharged for 50 MP!
# Kyrre was hit for 66 HP by Orc and now has 33 HP left!
# Kyrre has successfully cast ViewEarth and now has 35 MP!
# Solmyr
#   HP: 95
#   MP: 170
# Kyrre
#   HP: 33
#   MP: 35
#
# Input2:
# 4
# Adela 90 150
# SirMullich 70 40
# Ivor 1 111
# Tyris 94 61
# Heal - SirMullich - 50
# Recharge - Adela - 100
# CastSpell - Tyris - 1000 - Fireball
# TakeDamage - Tyris - 99 - Fireball
# TakeDamage - Ivor - 3 - Mosquito
# End
#
# Output2:
# SirMullich healed for 30 HP!
# Adela recharged for 50 MP!
# Tyris does not have enough MP to cast Fireball!
# Tyris has been killed by Fireball!
# Ivor has been killed by Mosquito!
# Adela
#   HP: 90
#   MP: 200
# SirMullich
#   HP: 100
#   MP: 40


def cast_spell(heroes_dict, split_command):
    current_hero_name = split_command[1]
    mana_points_needed = int(split_command[2])
    spell_name = split_command[3]

    if heroes_dict[current_hero_name]['MANA_POINTS'] >= mana_points_needed:
        heroes_dict[current_hero_name]['MANA_POINTS'] -= mana_points_needed
        print(f"{current_hero_name} has successfully cast {spell_name} and now has {heroes_dict[current_hero_name]['MANA_POINTS']} MP!")

    else:
        print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")

    return heroes_dict


def take_damage(heroes_dict, split_command):
    current_hero_name = split_command[1]
    damage = int(split_command[2])
    attacker = split_command[3]

    heroes_dict[current_hero_name]['HIT_POINTS'] -= damage

    if heroes_dict[current_hero_name]['HIT_POINTS'] > 0:
        print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[current_hero_name]['HIT_POINTS']} HP left!")

    else:
        print(f"{current_hero_name} has been killed by {attacker}!")
        del heroes_dict[current_hero_name]

    return heroes_dict


def recharge(heroes_dict, split_command):
    current_hero_name = split_command[1]
    amount = int(split_command[2])

    recovered_amount = amount
    heroes_dict[current_hero_name]['MANA_POINTS'] += amount

    if heroes_dict[current_hero_name]['MANA_POINTS'] > 200:
        recovered_amount = amount - (heroes_dict[current_hero_name]['MANA_POINTS'] - 200)
        heroes_dict[current_hero_name]['MANA_POINTS'] = 200

    print(f"{current_hero_name} recharged for {recovered_amount} MP!")

    return heroes_dict


def heal(heroes_dict, split_command):
    current_hero_name = split_command[1]
    amount = int(split_command[2])

    recovered_amount = amount
    heroes_dict[current_hero_name]['HIT_POINTS'] += amount

    if heroes_dict[current_hero_name]['HIT_POINTS'] > 100:
        recovered_amount = amount - (heroes_dict[current_hero_name]['HIT_POINTS'] - 100)
        heroes_dict[current_hero_name]['HIT_POINTS'] = 100

    print(f"{current_hero_name} healed for {recovered_amount} HP!")

    return heroes_dict


heroes = {}
number_of_heroes = int(input())

for hero in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {"HIT_POINTS": int(hit_points), "MANA_POINTS": int(mana_points)}

command = input()

while command != "End":
    command = command.split(" - ")

    if command[0] == "CastSpell":
        heroes = cast_spell(heroes, command)

    elif command[0] == "TakeDamage":
        heroes = take_damage(heroes, command)

    elif command[0] == "Recharge":
        heroes = recharge(heroes, command)

    elif command[0] == "Heal":
        heroes = heal(heroes, command)

    command = input()

for hero_name, values in heroes.items():
    print(hero_name)
    print(f"  HP: {values['HIT_POINTS']}")
    print(f"  MP: {values['MANA_POINTS']}")


# def create_heroes(heroes_dict, number):
#     for i in range(number):
#         data = input().split(" ")
#         hero_name = data[0]
#         hit_points = int(data[1])
#         mana_points = int(data[2])
#         heroes_dict[hero_name] = [hit_points, mana_points]
#
#
# def playing_game(heroes_dict):
#     while True:
#         command = input().split(" - ")
#
#         if command[0] == "End":
#             break
#
#         current_command = command[0]
#
#         if current_command == "CastSpell":
#             hero_name = command[1]
#             mp_needed = int(command[2])
#             spell_name = command[3]
#             available_mp = heroes_dict[hero_name][1]
#
#             if available_mp >= mp_needed:
#                 heroes_dict[hero_name][1] -= mp_needed
#                 current_mp = heroes_dict[hero_name][1]
#                 print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
#
#             else:
#                 print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#
#         elif current_command == "TakeDamage":
#             hero_name = command[1]
#             damage = int(command[2])
#             attacker = command[3]
#             available_hp = heroes_dict[hero_name][0]
#
#             if available_hp - damage > 0:
#                 heroes_dict[hero_name][0] -= damage
#                 current_hp = heroes_dict[hero_name][0]
#                 print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
#
#             else:
#                 del heroes_dict[hero_name]
#                 print(f"{hero_name} has been killed by {attacker}!")
#
#         elif current_command == "Recharge":
#             hero_name = command[1]
#             amount = int(command[2])
#             available_mp = heroes_dict[hero_name][1]
#
#             if available_mp + amount > 200:
#                 amount = 200 - available_mp
#                 heroes_dict[hero_name][1] += amount
#
#             else:
#                 heroes_dict[hero_name][1] += amount
#
#             print(f"{hero_name} recharged for {amount} MP!")
#
#         elif current_command == "Heal":
#             hero_name = command[1]
#             amount = int(command[2])
#             available_hp = heroes_dict[hero_name][0]
#
#             if available_hp + amount > 100:
#                 amount = 100 - available_hp
#                 heroes_dict[hero_name][0] += amount
#
#             else:
#                 heroes_dict[hero_name][0] += amount
#
#             print(f"{hero_name} healed for {amount} HP!")
#
#
# def print_function(heroes_dict):
#     print_result = ""
#
#     for hero in heroes_dict:
#         print_result += f"{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}\n"
#
#     return print_result
#
#
# def heroes_of_code(number):
#     heroes_dict = {}
#     create_heroes(heroes_dict, number_of_heroes)
#     playing_game(heroes_dict)
#     print(print_function(heroes_dict))
#
#
# number_of_heroes = int(input())
# heroes_of_code(number_of_heroes)
