capacity = int(input())
manager_messages = {}

while True:
    command = input()
    if command == 'Statistics':
        break
    action_list = command.split("=")
    current_action = action_list[0]
    if current_action == "Add":
        username = action_list[1]
        sent = int(action_list[2])
        received = int(action_list[3])
        if not username in manager_messages:
            manager_messages[username] = [sent, received]
    elif current_action == 'Message':
        sender = action_list[1]
        receiver = action_list[2]
        if sender in manager_messages and receiver in manager_messages:
            manager_messages[sender][0] += 1
            if sum(manager_messages[sender]) == capacity:
                print(f"{sender} reached the capacity!")
                del manager_messages[sender]
            manager_messages[receiver][1] += 1
            if sum(manager_messages[receiver]) == capacity:
                print(f"{receiver} reached the capacity!")
                del manager_messages[receiver]

    elif current_action == "Empty":
        username = action_list[1]
        if username == "All":
            manager_messages.clear()
        else:
            if username in manager_messages:
                del manager_messages[username]

print(f"Users count: {len(manager_messages)}")
for key, value in manager_messages.items():
    print(f'{key} - {sum(value)}')