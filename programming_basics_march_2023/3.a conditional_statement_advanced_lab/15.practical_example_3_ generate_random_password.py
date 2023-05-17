from string import   ascii_letters, digits, punctuation
import random

signs = ascii_letters + digits + punctuation
password_lenght = 10

password = ''.join(random.sample(signs, password_lenght))
print('Your new generated password is:', password)
