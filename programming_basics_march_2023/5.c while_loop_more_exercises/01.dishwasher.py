bottles_detergent = int(input())
wash_cycles = 1
plates = 0
pots = 0

volume_detergent = 750 * bottles_detergent

while volume_detergent >= 0:
    command = input()
    if command == 'End':
        break

    current_number = int(command)

    if wash_cycles % 3 == 0:
        pots += current_number
        volume_detergent -= current_number * 15
    else:
        plates += current_number
        volume_detergent -= current_number * 5
    wash_cycles += 1

if volume_detergent >= 0:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {abs(volume_detergent)} ml.')
else:
    print(f'Not enough detergent, {abs(volume_detergent)} ml. more necessary!')
