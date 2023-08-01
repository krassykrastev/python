liked_meals = {}
unliked_meals = 0

while True:
    command = input()

    if command == "Stop":
        break

    command_type, guest, meal = command.split("-")

    if command_type == "Like":
        liked_meals[guest] = liked_meals.get(guest, [])

        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)

    elif command_type == "Dislike":
        if guest not in liked_meals:
            print(f"{guest} is not at the party.")

        elif meal not in liked_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        elif meal in liked_meals[guest]:
            liked_meals[guest].remove(meal)
            unliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")

if liked_meals:
    for guest in liked_meals:
        print(f"{guest}: {', '.join(liked_meals[guest])}")

print(f"Unliked meals: {unliked_meals}")
