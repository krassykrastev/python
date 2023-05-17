fuel_type = input()
fuel_litters = float(input())
club_card = input()
fuel_price = 0
discount = 0

if fuel_type == "Gasoline":
    fuel_price = fuel_litters * 2.22
    if club_card == "Yes":
        fuel_price = fuel_litters * (2.22 - 0.18)
elif fuel_type == "Diesel":
    fuel_price = fuel_litters * 2.33
    if club_card == "Yes":
        fuel_price = fuel_litters * (2.33 - 0.12)
elif fuel_type == "Gas":
    fuel_price = fuel_litters * 0.93
    if club_card == "Yes":
        fuel_price = fuel_litters * (0.93 - 0.08)

if 20 <= fuel_litters <= 25:
    fuel_price = fuel_price - fuel_price * 0.08

elif fuel_litters > 25:
    fuel_price = fuel_price - fuel_price * 0.10

print(f'{fuel_price:.2f} lv.')
