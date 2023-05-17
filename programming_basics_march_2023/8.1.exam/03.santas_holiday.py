days_staying = int(input())
room_type = input()
score = input()

nights_staying = days_staying - 1

if room_type == 'room for one person':
    price = 18.00
elif room_type == 'apartment':
    price = 25.00
    if nights_staying < 10:
        price *= 0.70
    elif nights_staying < 15:
        price *= 0.65
    else:
        price *= 0.50
elif room_type == 'president apartment':
    price = 35.00
    if nights_staying < 10:
        price *= 0.90
    elif nights_staying < 15:
        price *= 0.85
    else:
        price *= 0.80

total_price = nights_staying * price

if score == 'positive':
    total_price *= 1.25

elif score == 'negative':
    total_price *= 0.90

print(f'{total_price:.2f}')
