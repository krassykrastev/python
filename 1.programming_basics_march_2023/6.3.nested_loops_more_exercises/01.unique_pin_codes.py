num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

for i in range(1, num_1 + 1):
    if i % 2 == 0:
        for j in range(2, num_2 + 1):
            prime = True
            for k in range(2, j):
                if j % k == 0:
                    prime = False
            if prime:
                for y in range(1, num_3 + 1):
                    if y % 2 == 0:
                        print(f'{i} {j} {y}')
