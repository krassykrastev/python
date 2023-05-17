width = int(input())
length = int(input())

cake_pieces = width * length

while cake_pieces > 0:
    command = input()
    if command == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break
    cake_pieces -= int(command)

if cake_pieces <= 0:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
