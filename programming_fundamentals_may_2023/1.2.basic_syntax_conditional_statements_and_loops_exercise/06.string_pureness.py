number_n = int(input())

for i in range (number_n):
    current_string = input()
    pure_string = True
    for j in current_string:
        if j == ',' or j == '_' or j == '.':
            pure_string = False
    if pure_string:
        print(f'{current_string} is pure.')
    else:
        print(f'{current_string} is not pure!')
