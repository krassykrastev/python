line = input()
followers = {}
while not line == "Log out":
    data = line.split(": ")
    command = data[0]
    username = data[1]
    if command == "New follower":
        if username not in followers:
            followers[username] = [0, 0]
    elif command == "Like":
        likes = int(data[2])
        if username not in followers:
            followers[username] = [0, 0]
        followers[username][0] += likes
    elif command == "Comment":
        if username not in followers:
            followers[username] = [0, 0]
        followers[username][1] += 1
    elif command == "Blocked":
        if username in followers:
            followers.pop(username)
        else:
            print(f"{username} doesn't exist.")

    line = input()

print(f"{len(followers)} followers")
for name, l_c in sorted(followers.items(), key=lambda x: (-sum(x[1]), x[0])):
    print(f"{name}: {sum(l_c)}")