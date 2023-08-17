capacity = int(input())
line = input()
users = {}
while not line == "Statistics":
    data = line.split("=")
    command = data[0]
    if command == "Add":
        username = data[1]
        sent = int(data[2])
        received = int(data[3])
        if username not in users:
            users[username] = [sent, received]
    elif command == "Message":
        sender = data[1]
        receiver = data[2]
        if sender in users and receiver in users:
            users[sender][0] += 1
            users[receiver][1] += 1
        if sum(users[sender]) >= capacity:
            users.pop(sender)
            print(f"{sender} reached the capacity!")
        if sum(users[receiver]) >= capacity:
            users.pop(receiver)
            print(f"{receiver} reached the capacity!")
    elif command == "Empty":
        username = data[1]
        if username == "All":
            users.clear()
        elif username in users:
            users.pop(username)
    line = input()

print(f"Users count: {len(users)}")

for user, sent_received in sorted(users.items(), key=lambda x: (-(x[1][1]), x[0])):
    print(f"{user} - {sum(sent_received)}")