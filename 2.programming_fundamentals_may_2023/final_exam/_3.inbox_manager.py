line = input()
emails = {}
while not line == "Statistics":
    data = line.split("->")
    command = data[0]
    username = data[1]
    if command == "Add":
        if username not in emails:
            emails[username] = []
        else:
            print(f"{username} already registered!")
    elif command == "Send":
        email = data[2]
        if username in emails:
            emails[username].append(email)
        else:
            emails[username] = [email]
    elif command == "Delete":
        if username in emails:
            emails.pop(username)
        else:
            print(f"{username} not found!")
    line = input()

print(f"Users count: {len(emails)}")
for key, value in sorted(emails.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{key}")
    for val in value:
        print(f" - {val}")