username = input()

line = input()
while not line == "Sign up":
    data = line.split()
    command = data[0]
    if command == "Case":
        type = data[1]
        if type == "lower":
            username = username.lower()
            print(username)
        elif type == "upper":
            username = username.upper()
            print(username)
    elif command == "Reverse":
        start_i = int(data[1])
        end_i = int(data[2])
        if 0 <= start_i <= end_i < len(username):
            reversing = "".join(reversed(username[start_i:end_i + 1]))
            print(reversing)
    elif command == "Cut":
        substring = data[1]
        if substring in username:
            username = username.replace(substring, "", 1)
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = data[1]
        username = username.replace(char, "*")
        print(username)
    elif command == "Check":
        char = data[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    line = input()