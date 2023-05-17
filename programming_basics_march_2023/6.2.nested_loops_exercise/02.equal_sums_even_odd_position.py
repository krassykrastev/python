n1 = int(input())
n2 = int(input())

for number in range(n1, n2 + 1):
    sum_even = 0
    sum_odd = 0
    num_to_str = str(number)

    for i in range(len(num_to_str)):
        if i % 2 == 0:
            sum_even += int(num_to_str[i])
        else:
            sum_odd += int(num_to_str[i])

    if sum_even == sum_odd:
        print(number, end=' ')
