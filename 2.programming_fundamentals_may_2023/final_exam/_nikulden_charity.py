text = input()
command = input()
while command != 'Finish':
    command = command.split()
    if command[0] == 'Replace':
        current_char = command[1]
        new_char = command[2]
        text = text.replace(current_char, new_char)
        print(text)

    elif command[0] == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = list(text)
            del text[start_index:end_index + 1]
            text = ''.join(text)
            print(text)
        else:
            print("Invalid indexes!")

    elif command[0] == 'Make':
        sub_command = command[1]
        if sub_command == 'Upper':
            text = text.upper()
            print(text)
        elif sub_command == 'Lower':
            text = text.lower()
            print(text)

    elif command[0] == 'Check':
        string = command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif command[0] == 'Sum':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = list(text)
            counter = 0
            for i in text[start_index:end_index + 1]:
                counter += ord(i)
            print(counter)
            text = ''.join(text)
        else:
            print('Invalid indexes!')
    command = input()