# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1.
# You will receive a positive integer number as input.
#
# Input1: 4
# Output1: 1 1 2 4
#
# Input2: 8
# Output2: 1 1 2 4 7 13 24 44

def tribonacci_sequence(some_number):
    tribonacci_seq = []
    for i in range(1, some_number + 1):
        if i == 1:
            tribonacci_seq.append(i)
        elif i <= 3:
            tribonacci_seq.append(i - 1)
        else:
            tribonacci_seq.append(tribonacci_seq[i - 4] + tribonacci_seq[i - 3] + tribonacci_seq[i - 2])
    print(*tribonacci_seq)

number_of_digits = int(input())
tribonacci_sequence(number_of_digits)