# You have just bought the latest and greatest computer game – Need for Seed III.
# Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.
# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain.
# On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the
# following format: "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
# •	"Drive : {car} : {distance} : {fuel}":
#   o	You need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
#   o	If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel, and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
#   o	You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"
# •	"Refuel : {car} : {fuel}":
#   o	Refill the tank of your car.
#   o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up.
#   o	Print a message in the following format: "{car} refueled with {fuel} liters"
# •	"Revert : {car} : {kilometers}":
#   o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
#   o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
#
# Input1:
# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop
#
# Output1:
# Audi A6 driven for 543 kilometers. 47 liters of fuel consumed.
# Mercedes CLS driven for 94 kilometers. 11 liters of fuel consumed.
# Not enough fuel to make that ride
# Audi A6 refueled with 50 liters
# Mercedes CLS mileage decreased by 500 kilometers
# Audi A6 -> Mileage: 10000 kms, Fuel in the tank: 65 lt.
# Mercedes CLS -> Mileage: 10594 kms, Fuel in the tank: 24 lt.
# Volkswagen Passat CC -> Mileage: 45678 kms, Fuel in the tank: 5 lt.
#
# Input2:
# 4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop
#
# Output2:
# Not enough fuel to make that ride
# Aston Martin Valkryie driven for 99 kilometers. 23 liters of fuel consumed.
# Aston Martin Valkryie driven for 2 kilometers. 1 liters of fuel consumed.
# Time to sell the Aston Martin Valkryie!
# Lamborghini Veneno refueled with 1 liters
# Bugatti Veyron mileage decreased by 2000 kilometers
# Lamborghini Veneno -> Mileage: 11111 kms, Fuel in the tank: 75 lt.
# Bugatti Veyron -> Mileage: 10345 kms, Fuel in the tank: 67 lt.
# Koenigsegg CCXR -> Mileage: 67890 kms, Fuel in the tank: 12 lt.

cars_count = int(input())

fuel_by_car = {}
mileage_by_car = {}

for i in range(cars_count):
    car_arguments = input().split("|")
    car = car_arguments[0]
    mileage = int(car_arguments[1])
    fuel = int(car_arguments[2])

    fuel_by_car[car] = fuel
    mileage_by_car[car] = mileage

while True:
    line = input()

    if line == "Stop":
        break

    command_args = line.split(" : ")
    command = command_args[0]
    car = command_args[1]

    if command == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])

        if fuel > fuel_by_car[car]:
            print("Not enough fuel to make that ride")
            continue

        fuel_by_car[car] -= fuel
        mileage_by_car[car] += distance

        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if mileage_by_car[car] >= 100000:
            fuel_by_car.pop(car)
            mileage_by_car.pop(car)
            print(f"Time to sell the {car}!")

    elif command == "Refuel":
        fuel = int(command_args[2])
        fuel_before_refuel = fuel_by_car[car]

        fuel_by_car[car] = min(fuel_by_car[car] + fuel, 75)
        print(f"{car} refueled with {fuel_by_car[car] - fuel_before_refuel} liters")

    elif command == "Revert":
        kilometers = int(command_args[2])
        updated_mileage = mileage_by_car[car] - kilometers

        if updated_mileage < 10000:
            mileage_by_car[car] = 10000
        else:
            mileage_by_car[car] = updated_mileage
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in fuel_by_car.keys():
    fuel = fuel_by_car[car]
    mileage = mileage_by_car[car]

    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
