screening_type = input()
rows = int(input())
cols = int(input())

tickets = rows * cols
revenue = 0

if screening_type == 'Premiere':
    revenue += tickets * 12.00
elif screening_type == 'Normal':
    revenue += tickets * 7.50
elif screening_type == 'Discount':
    revenue += tickets * 5.00

print(f'{revenue:.2f} leva')
