archery_field = list(map(int, input().split('|')))

points = 0

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Game':
        break
    elif command == 'Reverse':
        archery_field = archery_field[::-1]
    elif command == 'Shoot':
        token = tokens[1].split('@')
        direction = token[0]
        start_idx = int(token[1])
        length = int(token[2])
        last_idx = start_idx + length

        if direction == 'Left':
            new_field = archery_field[start_idx:] + archery_field[:start_idx]
            if 0 <= start_idx < len(new_field):
                new_field = new_field[::-1]
                while length >= 0:

                    for i, j in enumerate(archery_field):
                        length -= 1
                        if length == 0:
                            if j >= 5:
                                archery_field[i] -= 5
                                points += 5
                            elif 5 > j > 0:
                                points += archery_field[i]
                                archery_field[i] = 0

                        elif length < 0:
                            break

                        else:
                            continue

                new_field = archery_field[length:]+archery_field[start_idx:length]
                new_field = new_field[::-1]
                archery_field = new_field

        elif direction == 'Right':
            pass