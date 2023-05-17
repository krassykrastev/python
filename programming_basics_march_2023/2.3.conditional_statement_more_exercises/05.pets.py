from math import ceil, floor
number_of_days = int(input())
food_left_in_kg = int(input())
dogfood_per_day_in_kg = float(input())
catfood_per_day_in_kg = float(input())
turtlefood_per_day_in_gr = float(input())

food_needed = ((dogfood_per_day_in_kg + catfood_per_day_in_kg) + (turtlefood_per_day_in_gr / 1000)) * number_of_days
diff = abs(food_needed - food_left_in_kg)

if food_needed <= food_left_in_kg:
    print(f'{floor(diff)} kilos of food left.')

else:
    print(f'{ceil(diff)} more kilos of food are needed.')
