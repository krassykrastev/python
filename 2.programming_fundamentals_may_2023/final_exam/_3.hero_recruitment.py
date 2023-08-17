# Create a program that keeps track of enrolled heroes and their collection of spells (spellbook).
# You will be receiving the following commands until you receive the command "End":
#
# "Enroll {HeroName}":
# •	Adds the hero to your collection of heroes.
# •	If the hero is already present in your collection, print: "{HeroName} is already enrolled."
# "Learn {HeroName} {SpellName}":
# •	Adds the {SpellName} to the {HeroName}'s spellbook.
# •	If the {HeroName} doesn’t exist in the collection, print: "{HeroName} doesn't exist."
# •	If the hero already has the spell in his spellbook print: "{HeroName} has already learnt {SpellName}."
# "Unlearn {HeroName} {SpellName}":
# •	Remove the {SpellName} from the {HeroName}'s spellbook.
# •	If the {HeroName} doesn’t exist in the collection, print: "{HeroName} doesn't exist."
# •	If the {SpellName} doesn't exist in the hero's spellbook, print: "{HeroName} doesn't know {SpellName}."
#
# After you receive the "End" command, print all the heroes sorted by their count of spells in descending and then by the hero name ascending in the format described below:
#
# "Heroes:
# == {name1}: {spell1}, {spell2}, {spelln}
# == {name2}: {spell1}, {spell2}, {spelln}
# ...
# == {nameN}: {spell1}, {spell2}, {spelln}
#
# Input1:
# Enroll Stefan
# Enroll Pesho
# Enroll Stefan
# Learn Stefan ItShouldWork
# Learn Stamat ItShouldNotWork
# Unlearn Gosho Dispel
# Unlearn Stefan ItShouldWork
# End
#
# Output1:
# Stefan is already enrolled.
# Stamat doesn't exist.
# Gosho doesn't exist.
# Heroes:
# == Pesho:
# == Stefan:
#
# Input2:
# Enroll Stefan
# Learn Stefan ItShouldWork
# Learn Stefan ItShouldWork
# Unlearn Stefan NotFound
# End
#
# Output2:
# Stefan has already learnt ItShouldWork.
# Stefan doesn't know NotFound.
# Heroes:
# == Stefan: ItShouldWork

args = input()
heroes = {}

while args != "End":
    command = args.split()[0]
    heroname = args.split()[1]
    if command == 'Enroll':
        if heroname not in heroes:
            heroes[heroname] = []
        else:
            print(f'{heroname} is already enrolled.')
    elif command == 'Learn':
        spellname = args.split()[2]
        if heroname not in heroes:
            print(f"{heroname} doesn\'t exist.")
        elif spellname in heroes[heroname]:
            print(f'{heroname} has already learnt {spellname}.')
        else:
            heroes[heroname].append(spellname)
    elif command == 'Unlearn':
        spellname = args.split()[2]
        if heroname not in heroes:
            print(f"{heroname} doesn\'t exist.")
        elif spellname not in heroes[heroname]:
            print(f'{heroname} doesn\'t know {spellname}.')
        else:
            heroes[heroname].remove(spellname)
    args = input()
heroes = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))

print("Heroes:")
for key, value in heroes.items():
    print(f'== {key}: {", ".join(value)}')

# heroes_spells = {}
# while True:
#     command = input()
#     if command == 'End':
#         break
#     action = command.split(' ')
#     if action[0] == 'Enroll':
#         hero_name = action[1]
#         if hero_name not in heroes_spells:
#             heroes_spells[hero_name] = []
#         else:
#             print(f"{hero_name} is already enrolled.")
#
#     elif action[0] == 'Learn':
#         hero_name = action[1]
#         spell = action[2]
#         if hero_name not in heroes_spells:
#             print(f"{hero_name} doesn't exist.")
#         elif spell in heroes_spells[hero_name]:
#             print(f"{hero_name} has already learnt {spell}.")
#         else:
#             heroes_spells[hero_name].append(spell)
#
#     elif action[0] == 'Unlearn':
#         hero_name = action[1]
#         spell = action[2]
#         if hero_name not in heroes_spells:
#             print(f"{hero_name} doesn't exist.")
#         elif spell not in heroes_spells[hero_name]:
#             print(f"{hero_name} doesn't know {spell}.")
#         else:
#             heroes_spells[hero_name].remove(spell)
#
# print("Heroes:")
# for hero, spells in heroes_spells.items():
#     print(f"== {hero}: {', '.join(spells)}")