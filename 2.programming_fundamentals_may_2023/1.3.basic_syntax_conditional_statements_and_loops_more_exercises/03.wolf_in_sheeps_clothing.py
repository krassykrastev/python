sheep = 0

text = input()
my_list = list(text.split(', '))

for i in range(len(my_list) -1 , -1, -1):
    if my_list[-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    if my_list[i] == 'sheep':
        sheep += 1
    if my_list[i] == 'wolf':
        print(f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!')

# another solution from user:subtotal
# sheep_list = list(reversed(input().split(', ')))
#
# if sheep_list[0] == 'wolf':
#     print('Please go away and stop eating my sheep')
# else:
#     index = sheep_list.index('wolf')
#     print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')