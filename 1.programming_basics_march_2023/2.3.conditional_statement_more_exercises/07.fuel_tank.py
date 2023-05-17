fuel_type = input()
fuel_liters_in_tank = float(input())
msg = ""
mark = ""

if fuel_liters_in_tank >= 25:
    msg = "You have enough"
    mark = "."

elif fuel_liters_in_tank < 25:
    msg = "Fill your tank with"
    mark = "!"

if fuel_type == "Diesel":
    print(f'{msg} diesel{mark}')

elif fuel_type == "Gasoline":
    print(f'{msg} gasoline{mark}')

elif fuel_type == "Gas":
    print(f'{msg} gas{mark}')

else:
    print('Invalid fuel!')
