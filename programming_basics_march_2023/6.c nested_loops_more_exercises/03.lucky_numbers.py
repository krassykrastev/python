number = int(input())
lucky_number = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a + b == c + d:
                    lucky_number = int(f'{a}{b}{c}{d}')
                    if number % (a + b) == 0:
                        print(lucky_number, end=" ")
