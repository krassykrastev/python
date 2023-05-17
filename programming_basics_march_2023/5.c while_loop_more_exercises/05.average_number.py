n = int(input())
numbers_sum = 0

for i in range(n):
    current_number = int(input())
    numbers_sum += current_number

average = numbers_sum / n
print(f'{average:.2f}')
