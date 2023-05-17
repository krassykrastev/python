days_of_stay = int(input())
room_type = input()
score = input()

price = 0
nights = days_of_stay -1

if room_type == 'room for one person':
    price = nights * 18.00
elif room_type == 'apartment':
    price = nights * 25.00
    if nights < 10:
        price *= 0.70
    elif 10 < nights < 15:
        price *= 0.65
    elif nights > 15:
        price *= 0.50
elif room_type == 'president apartment':
    price = nights * 35.00
    if nights < 10:
        price *= 0.90
    elif 10 < nights < 15:
        price *= 0.85
    elif nights > 15:
        price *= 0.80

if score == 'positive':
    price = price + (0.25 * price)
elif score == 'negative':
    price = price - (0.10 * price)

print(f'{price:.2f}')
