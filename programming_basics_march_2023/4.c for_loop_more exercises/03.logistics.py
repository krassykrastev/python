number_of_cargo = int(input())
total_weight_in_tons = 0
p1 = 0
p2 = 0
p3 = 0
m = 0
k = 0
v = 0

for i in range(number_of_cargo):
    current_weight_in_tons = int(input())
    total_weight_in_tons += current_weight_in_tons

    if current_weight_in_tons <= 3:
        p1 += 200 * current_weight_in_tons
        m += current_weight_in_tons
    elif current_weight_in_tons <= 11:
        p2 += 175 * current_weight_in_tons
        k += current_weight_in_tons
    elif current_weight_in_tons >= 12:
        p3 += 120 * current_weight_in_tons
        v += current_weight_in_tons

total_price = p1 + p2 + p3
p1_percent = m / total_weight_in_tons * 100
p2_percent = k / total_weight_in_tons * 100
p3_percent = v / total_weight_in_tons * 100

print(f'{total_price / total_weight_in_tons:.2f}')
print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
