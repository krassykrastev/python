price_for_kg_veg = float(input())
price_for_kg_fruits = float(input())
total_kg_veg = int(input())
total_kg_fruits = int(input())
eur = 1.94

income_veg_bgn = price_for_kg_veg * total_kg_veg
income_fruit_bgn = price_for_kg_fruits * total_kg_fruits
total_income_eur = (income_fruit_bgn + income_veg_bgn) / eur

print(f'{total_income_eur:.2f}')
