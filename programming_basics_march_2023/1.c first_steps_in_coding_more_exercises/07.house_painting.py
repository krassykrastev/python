x = float(input())
y = float (input())
h = float(input())

area_front = (x * x) - (1.2 * 2)
area_back = x ** 2
side = (x * y) - (1.5 ** 2)

area_for_green_paint = area_front + area_back + (2 * side)
area_for_red_paint = 2 * (x * y) + 2 * (x * h / 2)

green_paint_needed = area_for_green_paint / 3.4
red_paint_needed = area_for_red_paint / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')
