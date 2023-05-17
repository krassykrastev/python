num_days = int(input())
num_hrs = int(input())

total_price = 0

for i in range(1, num_days + 1):
    price = 0
    for j in range(1, num_hrs + 1):
        if i % 2 == 0 and j % 2 != 0:
            price += 2.50
        elif i % 2 != 0 and j % 2 == 0:
            price += 1.25
        else:
            price += 1
    print(f'Day: {i} - {price:.2f} leva')
    total_price += price
print(f'Total: {total_price:.2f} leva')
