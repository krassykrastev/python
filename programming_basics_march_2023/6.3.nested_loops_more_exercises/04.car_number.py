first_number = int(input())
last_number = int(input())

for a in range(first_number, last_number + 1):
    for b in range(first_number, last_number + 1):
        for c in range(first_number, last_number + 1):
            for d in range(first_number, last_number + 1):
                if (a % 2 == 0 and d % 2 != 0) and (a > d) and ((b + c) % 2 == 0):
                    print(f'{a}{b}{c}{d}', end=' ')
                elif (a % 2 != 0 and d % 2 == 0) and (a > d) and ((b + c) % 2 == 0):
                    print(f'{a}{b}{c}{d}', end=' ')
