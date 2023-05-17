month = input()
nights = int(input())
price_studio = 0
price_apt = 0

if month == 'May' or month == 'October':
    price_studio = nights * 50
    price_apt = nights * 65
    if 14 > nights > 7:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.70
        price_apt *= 0.90
elif month == 'June' or month == 'September':
    price_studio = nights * 75.20
    price_apt = nights * 68.70
    if nights > 14:
        price_studio *= 0.80
        price_apt *= 0.90
elif month == 'July' or month == 'August':
    price_studio = nights * 76
    price_apt = nights * 77
    if nights > 14:
        price_apt *= 0.90
print(f'Apartment: {price_apt:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')
