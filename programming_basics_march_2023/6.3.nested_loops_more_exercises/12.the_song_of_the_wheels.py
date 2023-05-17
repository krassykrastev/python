control_value = int(input())

wheel = 0
password = ''

for a in range(1, 10):
    no_such_number = False
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * b) + (c * d) == control_value and a < b and c > d:
                    print(f'{a}{b}{c}{d}', end=' ')
                    wheel += 1
                    if wheel == 4:
                        password = f'{a}{b}{c}{d}'
if password == '':
    if wheel == 0:
        print(f'No!')
    elif 0 < wheel < 4:
        print()
        print(f'No!')

else:
    print()
    print(f'Password: {password}')
