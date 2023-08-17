text = input()
new_list = [el for el in text]


def chars(data: list):
    valid = True
    for element in data:
        if not element.isalnum() and not element == "_":
            valid = False
            break
    return valid


def is_upper(data: list):
    valid = False
    word = ''.join(data)
    for element in word:
        if element.isupper():
            valid = True
            break
    return valid


def is_lower(data: list):
    valid = False
    word = ''.join(data)
    for element in word:
        if element.islower():
            valid = True
            break
    return valid


def is_digit(data: list):
    valid = False
    for element in data:
        if element.isdigit():
            valid = True
            break
    return valid


while True:
    command = input()
    if command == 'Complete':
        break
    action_list = command.split()
    current_action = action_list[0]
    if current_action == "Make" and action_list[1] == "Upper":
        i_text = int(action_list[2])
        new_list[i_text] = new_list[i_text].upper()
        print(''.join(new_list))
    elif current_action == 'Make' and action_list[1] == "Lower":
        i_text = int(action_list[2])
        new_list[i_text] = new_list[i_text].lower()
        print(''.join(new_list))
    elif current_action == 'Insert':
        index = int(action_list[1])
        char = action_list[2]
        if index in range(len(new_list)):
            new_list.insert(index, char)
            print(''.join(new_list))
    elif current_action == 'Replace':
        char = action_list[1]
        value = int(action_list[2])
        to_replace = ord(char) + value
        password = ''.join(new_list)
        password = password.replace(char, chr(to_replace))
        new_list = [el for el in password]
        print(''.join(new_list))
    elif current_action == 'Validation':
        if len(new_list) < 8:
            print("Password must be at least 8 characters long!")
        validator_1 = chars(new_list)
        if validator_1 == False:
            print("Password must consist only of letters, digits and _!")
        validator_2 = is_upper(new_list)
        if validator_2 == False:
            print("Password must consist at least one uppercase letter!")
        validator_3 = is_lower(new_list)
        if validator_3 == False:
            print("Password must consist at least one lowercase letter!")
        validator_4 = is_digit(new_list)
        if validator_4 == False:
            print("Password must consist at least one digit!")