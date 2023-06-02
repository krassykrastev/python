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