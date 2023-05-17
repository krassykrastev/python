num = int(input())
result = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0

for i in range(num):
    current_num = int(input())
    if current_num < 0 or current_num > 50:
        result /= 2
        p1 += 1
    elif current_num <= 9:
        result += current_num * 0.20
        p2 += 1
    elif current_num <= 19:
        result += current_num * 0.30
        p3 += 1
    elif current_num <= 29:
        result += current_num * 0.40
        p4 += 1
    elif current_num <= 39:
        result += 50
        p5 += 1
    elif current_num <= 50:
        result += 100
        p6 += 1

p1_percentage = p1 / num * 100
p2_percentage = p2 / num * 100
p3_percentage = p3 / num * 100
p4_percentage = p4 / num * 100
p5_percentage = p5 / num * 100
p6_percentage = p6 / num * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {p2_percentage:.2f}%')
print(f'From 10 to 19: {p3_percentage:.2f}%')
print(f'From 20 to 29: {p4_percentage:.2f}%')
print(f'From 30 to 39: {p5_percentage:.2f}%')
print(f'From 40 to 50: {p6_percentage:.2f}%')
print(f'Invalid numbers: {p1_percentage:.2f}%')
