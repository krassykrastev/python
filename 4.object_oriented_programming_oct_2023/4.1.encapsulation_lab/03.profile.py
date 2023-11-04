# Create a class called Profile. Upon initialization, it should receive:
# •	username: str - the username should be between 5 and 15 characters (inclusive). If it is not, raise a ValueError
# with the message "The username must be between 5 and 15 characters."
# •	password: str - the password must be at least 8 characters long; it must contain at least one upper case letter and
# at least one digit. If it does not, raise a ValueError with the message "The password must be 8 or more characters
# with at least 1 digit and 1 uppercase letter."
# Hint: Use Getters and Setters to name-mangle them.
# Override the __str__() method of the base class, so it returns: "You have a profile with username: "{username}" and
# password: {"*" with the length of password}".
#
# Test code1:
# profile_with_invalid_password = Profile('My_username', 'My-password')
#
# Output1:
# ValueError: The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.
#
# Test code2:
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
#
# Output2:
# ValueError: The username must be between 5 and 15 characters.
#
# Test code3:
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
#
# Output3:
# You have a profile with username: "Username" and password: ********

class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) >= 5 and len(value) <= 15:
            self.__username = value
        else:
            raise ValueError(f"The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        is_valid_length = len(value) >= 8
        is_upper_case = [char for char in value if char.isupper()]
        is_digit_presented = any([char for char in value if char.isdigit()])

        if is_valid_length and is_upper_case and is_digit_presented:
            self.__password = value
        else:
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')
profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
