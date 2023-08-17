decrypted_message = input()
while True:
    command = input()
    if command == 'Finish':
        break
    action = command.split(' ')

    if action[0] == 'Replace':
        current_char = action[1]
        new_char = action[2]
        decrypted_message = decrypted_message.replace(current_char, new_char)

    elif action[0] == 'Cut':
        start_index = int(action[1])
        end_index = int(action[2])
        if start_index < 0 or end_index >= len(decrypted_message):
            print('Invalid indices!')
            continue
        else:
            decrypted_message = decrypted_message[:start_index] + decrypted_message[end_index + 1:]

    elif action[0] == 'Make':
        upper_lower = action[1]
        if upper_lower == 'Upper':
            decrypted_message = decrypted_message.upper()
        elif upper_lower == 'Lower':
            decrypted_message = decrypted_message.lower()

    elif action[0] == 'Check':
        string = action[1]
        if string in decrypted_message:
            print(f"Message contains {string}")
            continue
        else:
            print(f"Message doesn't contain {string}")
            continue

    elif action[0] == 'Sum':
        start_index = int(action[1])
        end_index = int(action[2])
        total = 0
        if start_index < 0 or end_index >= len(decrypted_message):
            print('Invalid indices!')
            continue
        else:
            for i in range(start_index, end_index + 1):
                total += ord(decrypted_message[i])
            print(total)
            continue

    print(decrypted_message)