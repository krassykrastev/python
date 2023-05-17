number_guys = int(input())
number_girls = int(input())
number_tables = int(input())
combinations = 0

for a in range(1, number_guys + 1):
    for b in range(1, number_girls + 1):
        combinations += 1
        if combinations <= number_tables:
            print(f'({a} <-> {b})', end=" ")
