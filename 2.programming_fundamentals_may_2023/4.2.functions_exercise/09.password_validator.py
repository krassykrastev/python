# Write a function that checks if a given password is valid. Password validations are:
# • It should be 6 - 10 (inclusive) characters long
# • It should consist only of letters and digits
# • It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# • "Password must be between 6 and 10 characters"
# • "Password must consist only of letters and digits"
# • "Password must have at least 2 digits"
#
# Input1: logIn
# Output1:
# Password must be between 6 and 10 characters
# Password must have at least 2 digits
#
# Input2: MyPass123
# Output2: Password is valid
#
# Input3: Pa$s$s
# Output3:
# Password must consist only of letters and digits
# Password must have at least 2 digits

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