list_of_gifts = input().split(' ')

while True:
    commands = input().split(' ')
    if commands == ['No', 'Money']:
        break
    elif 'OutOfStock' in commands:
        for i in range(len(list_of_gifts)):
            if list_of_gifts[i] == commands[1]:
                list_of_gifts[i] = 'None'
    elif 'Required' in commands:
        if 0 <= int(commands[2]) < len(list_of_gifts):
            list_of_gifts[int(commands[2])] = commands[1]
    elif 'JustInCase' in commands:
        list_of_gifts[-1] = commands[1]

for gift in list_of_gifts:
    if gift != 'None':
        print(gift, end= ' ')