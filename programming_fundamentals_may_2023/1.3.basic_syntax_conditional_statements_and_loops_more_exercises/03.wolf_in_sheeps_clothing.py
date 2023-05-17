sheep = 0

text = input()
my_list = list(text.split(', '))

for i in range(len(my_list) -1 , -1, -1):
    if i == len(my_list) -1 and my_list[i] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    if my_list[i] == 'sheep':
        sheep += 1
    if my_list[i] == 'wolf':
        print(f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!')
