colored_eggs = 0
current_bread_count = 0

budget = float(input())
price_for_1kg_flor = float(input())
price_for_1pack_eggs = 0.75 * price_for_1kg_flor
price_for_1l_milk = 1.25 * price_for_1kg_flor
recipe_cost = price_for_1kg_flor + price_for_1pack_eggs + 0.25 * price_for_1l_milk

while budget >= recipe_cost:
    budget -= recipe_cost
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2

print(f'You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
