num_pairs = int(input())

prev_sum = 0
sum_of_both = 0
current_diff = 0
max_diff = 0
equal_pairs = True

for i in range(num_pairs):
    first_num = int(input())
    second_num = int(input())
    sum_of_both = first_num + second_num
    if i > 0:
        current_diff = abs(sum_of_both - prev_sum)
        if current_diff > max_diff:
            max_diff = current_diff
        if sum_of_both != prev_sum:
            equal_pairs = False
    prev_sum = sum_of_both

if equal_pairs:
    print(f'Yes, value={sum_of_both}')
else:
    print(f'No, maxdiff={max_diff}')
