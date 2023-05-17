count_chicken = int(input())
count_fish = int(input())
count_veg = int(input())

total_price = (count_chicken * 10.35) + (count_fish * 12.40) + (count_veg * 8.15)
desert_price = total_price * 0.20

final_price = total_price + desert_price + 2.50

print(final_price)
