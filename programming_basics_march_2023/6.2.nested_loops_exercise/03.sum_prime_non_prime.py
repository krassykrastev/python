is_prime = True
prime_sum = 0
non_prime_sum = 0

input_line = input()
while input_line != 'stop':
    current_num = int(input_line)
    if current_num < 0:
        print('Number is negative.')
    else:
        for i in range(2, current_num):
            if current_num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_sum += current_num
        else:
            non_prime_sum += current_num
            is_prime = True
    input_line = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
