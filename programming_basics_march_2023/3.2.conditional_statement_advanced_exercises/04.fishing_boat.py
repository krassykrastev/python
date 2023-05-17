budget = int(input())
season = input()
fishermen_count = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fishermen_count <= 6:
    rent *= 0.9 #отстъпка 10%, т.е. 0.9 от цялата променлива
elif 7 < fishermen_count <=11:
    rent *= 0.85 #отстъпка 15%, т.е. 0.85 от цялата променлива
elif fishermen_count > 12:
    rent *= 0.75 #отстъпка 25%, т.е. 0.75 от цялата променлива

if fishermen_count % 2 == 0 and season != 'Autumn': #проверяваме дали числото е четно и сезона да не е Autumn
    rent *= 0.95 #отстъпка от 5% ако рибарите са четно число

diff = abs(rent - budget)

if rent > budget:
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    print(f'Yes! You have {diff:.2f} leva left.')
