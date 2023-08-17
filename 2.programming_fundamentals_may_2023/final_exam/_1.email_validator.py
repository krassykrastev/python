email = input()

line = input()
while not line == "Complete":
    data = line.split()
    command = data[0]
    if command == "Make":
        if data[1] == "Upper":
            email = email.upper()
            print(email)
        elif data[1] == "Lower":
            email = email.lower()
            print(email)
    elif command == "GetDomain":
        count = int(data[-1])
        print(email[-count:])
    elif command == "GetUsername":
        if "@" in email:
            i_symbol = email.index("@")
            print(email[:i_symbol])
        else:
            print(f"The email {email} doesnt contain the @ symbol")
    elif command == "Replace":
        char = data[-1]
        email = email.replace(char, "-")
        print(email)
    elif command == "Encrypt":
        print(" ".join([str(ord(el)) for el in email]))
    line = input()