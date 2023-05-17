first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

for a in range(first_pair_start, first_pair_start + first_pair_diff + 1):
    is_a_prime = True
    for aa in range(2, a):
        if a % aa == 0:
            is_a_prime = False

    for c in range(second_pair_start, second_pair_start + second_pair_diff + 1):
        is_c_prime = True
        for cc in range(2, c):
            if c % cc == 0:
                is_c_prime = False
        if is_a_prime and is_c_prime:
            print(f"{a}{c}")
