line = input()
time = {}
members = {}
total_time = 0
while not line == "start of concert":
    data = line.split("; ")
    command = data[0]
    band = data[1]

    if band not in members:
        members[band] = []
        time[band] = 0

    if command == "Add":
        names = data[2].split(", ")
        for member in names:
            if member not in members[band]:
                members[band].append(member)

    elif command == "Play":
        minutes = int(data[2])
        total_time += minutes
        time[band] += minutes
    line = input()

print(f"Total time: {total_time}")

for band, mins in sorted(time.items(), key=lambda x: (-x[1], x[0])):
    print(f"{band} -> {mins}")

band_name = input()
print(band_name)

for member_name in members[band_name]:
    print(f"=> {member_name}")