flowers_type = input()
flowers_count = int(input())
budget = int(input())

price = 0
discount = 0

if flowers_type == "Roses":
    price = 5
    if flowers_count > 80:
        discount += 0.10
elif flowers_type == "Dahlias":
    price = 3.80
    if flowers_count > 90:
        discount += 0.15
elif flowers_type == "Tulips":
    price = 2.80
    if flowers_count > 80:
        discount += 0.15
elif flowers_type == "Narcissus":
    price = 3.00
    if flowers_count < 120:
        discount -= 0.15
elif flowers_type == "Gladiolus":
    price = 2.50
    if flowers_count < 80:
        discount -= 0.20

total_price = flowers_count * price * (1 - discount)
diff = abs(total_price - budget)

if total_price > budget:
    print(f'Not enough money, you need {diff:.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {flowers_count} {flowers_type} and {diff:.2f} leva left.')
