# You have now returned from your world tour. On your way, you have discovered some new plants, and you want to gather
# some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines, you will be given some information about the
# plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it
# later. If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
#
# Input1:
# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
#
# Output1:
# Plants for the exhibition:
# - Arnoldii; Rarity: 4; Rating: 0.00
# - Woodii; Rarity: 5; Rating: 7.50
# - Welwitschia; Rarity: 2; Rating: 7.00
#
# Input2:
# 2
# Candelabra<->10
# Oahu<->10
# Rate: Oahu - 7
# Rate: Candelabra - 6
# Exhibition
#
# Output2:
# Plants for the exhibition:
# - Candelabra; Rarity: 10; Rating: 6.00
# - Oahu; Rarity: 10; Rating: 7.00

def create_plants_data(plants, number):
    for i in range(number):
        data = input().split("<->")
        name_of_plant = data[0]
        rarity = int(data[1])

        if name_of_plant not in plants:
            plants[name_of_plant] = {"rarity": rarity, "rating": []}

        else:
            plants[name_of_plant]["rarity"] += rarity

    return plants


def additional_plants_data(plants):

    while True:
        command = input().split(": ")

        if command[0] == "Exhibition":
            break

        data = command[1].split(" - ")
        type_of_command = command[0]
        plant = data[0]

        if plant not in plants:
            print("error")
            continue

        if type_of_command == "Rate":
            rating = int(data[1])
            plants[plant]["rating"].append(rating)

        elif type_of_command == "Update":
            new_rarity = int(data[1])
            plants[plant]["rarity"] = new_rarity

        elif type_of_command == "Reset":
            plants[plant]["rating"].clear()

    return plants


def print_function(plants):
    print("Plants for the exhibition:")

    for dict_el in plants:

        if len(plants[dict_el]["rating"]) > 0 and sum(plants[dict_el]["rating"]) > 0:
            average_rating = sum(plants[dict_el]["rating"]) / len(plants[dict_el]["rating"])

        else:
            average_rating = 0

        rarity = plants[dict_el]["rarity"]
        print(f"- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plant_discovery(number):
    plants = {}

    create_plants_data(plants, number)
    additional_plants_data(plants)
    print_function(plants)


n = int(input())
plant_discovery(n)
