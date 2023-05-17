count_pens = int(input())
count_markers = int(input())
liters_cleaner = int(input())
discount_percent = int(input())

sum_pens = count_pens * 5.80
sum_markers = count_markers * 7.20
sum_cleaner = liters_cleaner * 1.20

total_sum = sum_pens + sum_markers + sum_cleaner
discount = total_sum * (discount_percent / 100)
final_sum = total_sum - discount

print(final_sum)
