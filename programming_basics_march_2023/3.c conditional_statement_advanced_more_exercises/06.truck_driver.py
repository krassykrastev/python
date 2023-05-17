season = input()
kms_per_month = float(input())

revenue = 0

if season == 'Spring' or season == 'Autumn':
    if kms_per_month <= 5000:
        revenue = kms_per_month * 0.75 * 4
    elif 5000 < kms_per_month <= 10000:
        revenue = kms_per_month * 0.95 * 4
elif season == 'Summer':
    if kms_per_month <= 5000:
        revenue = kms_per_month * 0.90 * 4
    elif 5000 < kms_per_month <= 10000:
        revenue = kms_per_month * 1.10 * 4
elif season == 'Winter':
    if kms_per_month <= 5000:
        revenue = kms_per_month * 1.05 * 4
    elif 5000 < kms_per_month <= 10000:
        revenue = kms_per_month * 1.25 * 4

if 10000 < kms_per_month <= 20000:
    revenue = kms_per_month * 1.45 * 4

revenue *= 0.90

print(f'{revenue:.2f}')
