travel_route = input().split("||")
starting_amount_of_fuel = int(input())
starting_ammunition = int(input())

for command in travel_route:
    if command != "Titan":
        command = command.split(" ")
    else:
        print("You have reached Titan, all passengers are safe.")
        break
    if command[0] == "Travel":
        if starting_amount_of_fuel >= int(command[1]):
            starting_amount_of_fuel -= int(command[1])
            print(f"The spaceship travelled {int(command[1])} light-years.")
        else:
            print("Mission failed.")
            break
    elif command[0] == "Enemy":
        if starting_ammunition >= int(command[1]):
            starting_ammunition -= int(command[1])
            print(f"An enemy with {int(command[1])} armour is defeated.")
        elif starting_amount_of_fuel >= int(command[1]) * 2:
            starting_amount_of_fuel -= int(command[1]) * 2
            print(f"An enemy with {int(command[1])} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif command[0] == "Repair":
        starting_amount_of_fuel += int(command[1])
        starting_ammunition += (int(command[1]) * 2)
        print(f"Ammunitions added: {int(command[1]) * 2}.")
        print(f"Fuel added: {int(command[1])}.")