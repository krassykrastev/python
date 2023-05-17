username = input()
password_DB = input()

current_password = input()

while password_DB != current_password:
    current_password = input()

print(f'Welcome {username}!')
