# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of
# Jack Daniels. Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas,
# looking for gold and treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and
# show them the pirate's way!
# Until the "Sail" command is given, you will be receiving:
# •	You and your crew have targeted cities, with their population and gold, separated by "||".
# •	If you receive a city that has already been received, you have to increase the population and gold with the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
#   o	You have successfully attacked and plundered the town, killing the given number of people and stealing the
#   respective amount of gold.
#   o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
#   o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# 	You need to remove it from your collection of targeted cities and print the following message:
# "{town} has been wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print:
# "Gold added cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the
# following message: "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
#
# Input1:
# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End
#
# Output1:
# Tortuga plundered! 380 gold stolen, 75000 citizens killed.
# 180 gold added to the city treasury. Santo Domingo now has 810 gold.
# Ahoy, Captain! There are 3 wealthy settlements to go to:
# Tortuga -> Population: 270000 citizens, Gold: 870 kg
# Santo Domingo -> Population: 240000 citizens, Gold: 810 kg
# Havana -> Population: 410000 citizens, Gold: 1100 kg
#
# Input2:
# Nassau||95000||1000
# San Juan||930000||1250
# Campeche||270000||690
# Port Royal||320000||1000
# Port Royal||100000||2000
# Sail
# Prosper=>Port Royal=>-200
# Plunder=>Nassau=>94000=>750
# Plunder=>Nassau=>1000=>150
# Plunder=>Campeche=>150000=>690
# End
#
# Output2:
# Gold added cannot be a negative number!
# Nassau plundered! 750 gold stolen, 94000 citizens killed.
# Nassau plundered! 150 gold stolen, 1000 citizens killed.
# Nassau has been wiped off the map!
# Campeche plundered! 690 gold stolen, 150000 citizens killed.
# Campeche has been wiped off the map!
# Ahoy, Captain! There are 2 wealthy settlements to go to:
# San Juan -> Population: 930000 citizens, Gold: 1250 kg
# Port Royal -> Population: 420000 citizens, Gold: 3000 kg

data = input()
cities = {}

while data != "Sail":
    splitted_data = data.split("||")
    city = splitted_data[0]
    population = int(splitted_data[1])
    gold = int(splitted_data[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}

    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    data = input()

data = input()

while data != "End":
    splitted_data = data.split("=>")
    command = splitted_data[0]
    city = splitted_data[1]

    if command == "Plunder":
        people = int(splitted_data[2])
        gold = int(splitted_data[3])

        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(splitted_data[2])
        if gold >= 0:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

        else:
            print("Gold added cannot be a negative number!")

    data = input()

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, value in cities.items():
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
