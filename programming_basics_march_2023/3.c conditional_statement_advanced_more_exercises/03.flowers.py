num_hrizantemi = int(input())
num_rozi = int(input())
num_laleta = int(input())
season = input()
holiday = input()

price = 0

if season == 'Spring' or season == 'Summer':
    price = num_hrizantemi * 2 + num_rozi * 4.10 + num_laleta * 2.50
    if holiday == "Y":
        price *= 1.15
    if num_laleta > 7 and season == 'Spring':
        price *= 0.95
    if num_hrizantemi + num_rozi + num_laleta > 20:
        price *= 0.80
elif season == 'Autumn' or season == 'Winter':
    price = num_hrizantemi * 3.75 + num_rozi * 4.50 + num_laleta * 4.15
    if holiday == "Y":
        price *= 1.15
    if num_rozi >= 10 and season == 'Winter':
        price *= 0.90
    if num_hrizantemi + num_rozi + num_laleta > 20:
        price *= 0.80

price += 2

print(f'{price:.2f}')
