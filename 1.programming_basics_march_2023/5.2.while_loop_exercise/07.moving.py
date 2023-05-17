space_width = int(input())
space_length = int(input())
space_height = int(input())

space_volume = space_width * space_length * space_height

while space_volume > 0:
    command = input()
    if command == 'Done':
        break
    space_volume -= int(command)

if space_volume > 0:
    print(f'{space_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(space_volume)} Cubic meters more.')
