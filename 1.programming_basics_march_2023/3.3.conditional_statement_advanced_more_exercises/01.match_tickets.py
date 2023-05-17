budget = float(input())
category = input()
people_num = int(input())

price = 0
transport = 0

if category == 'VIP':
    price = people_num * 499.99
    if 1 <= people_num <= 4:
        transport = budget * 0.75
    elif 5 <= people_num <= 9:
        transport = budget * 0.60
    elif 10 <= people_num <= 24:
        transport = budget * 0.50
    elif 25 <= people_num <= 49:
        transport = budget * 0.40
    elif people_num > 50:
        transport = budget * 0.25
elif category == 'Normal':
    price = people_num * 249.99
    if 1 <= people_num <= 4:
        transport = budget * 0.75
    elif 5 <= people_num <= 9:
        transport = budget * 0.60
    elif 10 <= people_num <= 24:
        transport = budget * 0.50
    elif 25 <= people_num <= 49:
        transport = budget * 0.40
    elif people_num > 50:
        transport = budget * 0.25

money_left = budget - transport
diff = abs(money_left - price)

if budget >= price + transport:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
