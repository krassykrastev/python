line = input()
guests = {}
unliked = 0
while not line == "Stop":
    data = line.split("-")
    state = data[0]
    guest = data[1]
    meal = data[2]
    if state == "Like":
        if guest not in guests:
            guests[guest] = [meal]
        elif guest in guests and meal not in guests[guest]:
            guests[guest].append(meal)
        elif meal in guests[guest]:
            line = input()
            continue
    elif state == "Unlike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
        elif guest in guests and meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection")
        else:
            unliked += 1
            print(f"{guest} doesn't like the {meal}.")
            guests[guest].remove(meal)
    line = input()

for key, value in sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{key}: {', '.join(value)}")

print(f"Unliked meals: {unliked}")