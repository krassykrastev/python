def validate_password(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False
    if not password.isalnum():
        print('Password must consist only of letters and digits')
        is_valid = False
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        print('Password must have at least 2 digits')
        is_valid = False
    return is_valid

some_password = input()
password_is_valid = validate_password(some_password)
if password_is_valid:
    print('Password is valid')