num_coins_1lv = int(input())
num_coins_2lv = int(input())
num_banknotes_5lv = int(input())
value_to_be_paid = int(input())

for a in range(num_coins_1lv + 1):
    for b in range(num_coins_2lv + 1):
        for c in range(num_banknotes_5lv + 1):
            if (a * 1) + (b * 2) + (c * 5) == value_to_be_paid:
                print(f'{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {value_to_be_paid} lv.')
