# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
# • coffee - 1.50
# • water - 1.00
# • coke - 1.40
# • snacks - 2.00
# Print the result formatted to the second decimal place.
#
# Input1:
# water
# 5
#
# Output1: 5.00
#
# Input2:
# coffee
# 2
#
# Output2: 3.00

def calculate_total_order_value(some_product):
    if some_product == 'coffee':
        return 1.50 * quantity
    elif some_product == 'water':
        return 1.00 * quantity
    elif some_product == 'coke':
        return 1.40 * quantity
    elif some_product == 'snacks':
        return 2.00 * quantity

product = input()
quantity = int(input())

print(f'{calculate_total_order_value(product):.2f}')