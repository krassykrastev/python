i = 0
num_k = int(input())
num_l = int(input())
num_m = int(input())
num_n = int(input())

for num1_first_number in range(num_k, 9):
    if i == 6:
        break
    for num1_second_number in range(9, num_l - 1, -1):
        if i == 6:
            break
        for num2_first_number in range(num_m, 9):
            if i == 6:
                break
            for num2_second_number in range(9, num_n - 1, -1):
                if i == 6:
                    break
                if (num1_first_number % 2 == 0 and num1_second_number % 2 != 0) and (num2_first_number % 2 == 0 and num2_second_number % 2 != 0):
                    if num1_first_number == num2_first_number and num1_second_number == num2_second_number:
                        print(f'Cannot change the same player.')
                    else:
                        print(f'{num1_first_number}{num1_second_number} - {num2_first_number}{num2_second_number}')
                        i += 1
