from math import ceil, floor
nr_magnolii = int(input())
nr_zumbuli = int(input())
nr_roses = int(input())
nr_cactus = int(input())
price_gift = float(input())

order = nr_magnolii * 3.25 + nr_zumbuli * 4 + nr_roses * 3.50 + nr_cactus * 8
after_tax = order - order * 0.05
diff = abs(after_tax - price_gift)

if after_tax < price_gift:
    print(f'She will have to borrow {ceil(diff)} leva.')
else:
    print(f'She is left with {floor(diff)} leva.')
