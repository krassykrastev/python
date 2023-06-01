def calculate_total_order_value():
    if product == 'coffee':
        return 1.50 * quantity
    elif product == 'water':
        return 1.00 * quantity
    elif product == 'coke':
        return 1.40 * quantity
    elif product == 'snacks':
        return 2.00 * quantity

product = input()
quantity = int(input())

print(f'{calculate_total_order_value():.2f}')