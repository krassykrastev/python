nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_needed = int(input())

sum_nylon = (nylon_needed + 2) * 1.50
sum_paint = (paint_needed + (paint_needed * 0.1)) * 14.50
sum_thinner = thinner_needed * 5.00

sum_materials = sum_nylon + sum_paint + sum_thinner + 0.4
worker_pay = sum_materials * 0.3 * hours_needed

total_sum = sum_materials + worker_pay

print(total_sum)
