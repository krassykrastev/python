budget = float(input())
number_of_extras = int(input())
price_for_clothing_per_extra = float(input())

price_decors = budget * 0.10
price_for_clothing = price_for_clothing_per_extra * number_of_extras

if number_of_extras > 150:
    price_for_clothing *= 0.90 #отстъпка от 10%, т.е. променливата е 0.9 от цялата стойност

total_costs = price_decors + price_for_clothing
diff = abs(total_costs - budget)

if total_costs <= budget:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')

else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
