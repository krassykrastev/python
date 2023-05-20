is_prime = False
number = int(input())
if number > 2:
    for i in range(2, number):
        if number % i == 0:
            is_prime = True
            break
if not is_prime:
    print('True')
else:
    print('False')