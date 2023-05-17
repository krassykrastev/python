drink = input()
sugar = input()
num_drinks = int(input())

price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1.00
    elif sugar == 'Extra':
        price = 1.20
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1.00
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60
elif drink == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

if sugar == 'Without':
    price *= 0.65

if drink == 'Espresso' and num_drinks >= 5:
    price *= 0.75

total_price = price * num_drinks

if total_price > 15:
    total_price *= 0.80

print(f'You bought {num_drinks} cups of {drink} for {total_price:.2f} lv.')
