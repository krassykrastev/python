stadium_capacity = int(input())
total_fens = int(input())

a = 0
b = 0
v = 0
g = 0

for i in range(total_fens):
    sector = input()
    if sector == 'A':
        a += 1
    elif sector == 'B':
        b += 1
    elif sector == 'V':
        v += 1
    elif sector == 'G':
        g += 1

a_percent = a / total_fens * 100
b_percent = b / total_fens * 100
v_percent = v / total_fens * 100
g_percent = g / total_fens * 100
total_percent = total_fens / stadium_capacity * 100

print(f'{a_percent:.2f}%')
print(f'{b_percent:.2f}%')
print(f'{v_percent:.2f}%')
print(f'{g_percent:.2f}%')
print(f'{total_percent:.2f}%')
