a = int(input())
b = int(input())
max_number_of_passwords = int(input())
A = 35
B = 64

number_of_passwords = 0

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if max_number_of_passwords > number_of_passwords:
            print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end="|")
            A += 1
            B += 1
            if A > 55: A = 35
            if B > 96: B = 64
            number_of_passwords += 1
        else:
            break
