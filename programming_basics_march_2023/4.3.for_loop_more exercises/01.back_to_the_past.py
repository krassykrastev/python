inherited_money = float(input())
year = int(input())
money_needed = 0

for i in range(1800, year + 1):
    if i % 2 == 0:
        money_needed += 12000
    else:
        money_needed += 12000 + (50 * (18 + (i - 1800)))

diff = abs(money_needed - inherited_money)

if inherited_money >= money_needed:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')

else:
    print(f'He will need {diff:.2f} dollars to survive.')
