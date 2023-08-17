import re
count_of_inputs = int(input())
successfull_registrations = 0
pattern = r'(U\$)([A-Z][a-z]{2,})(\1)(P@\$)([a-z]{5,}\d{1,})(\4)'

for i in range(count_of_inputs):
    registration = input()

    match = re.fullmatch(pattern, registration)

    if match is None:
        print("Invalid username or password")
        continue

    username = match[2]
    password = match[5]
    print("Registration was successful")
    print(f"Username: {username}, Password: {password}")
    successfull_registrations +=1

print(f"Successful registrations: {successfull_registrations}")