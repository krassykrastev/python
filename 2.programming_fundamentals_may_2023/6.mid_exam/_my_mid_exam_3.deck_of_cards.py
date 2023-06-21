cards = input().split(", ")
number_of_cards = int(input())

for card in range(number_of_cards):
    command = input().split(", ")

    if command[0] == "Add":
        if command[1] in cards:
            print("Card is already in the deck")
        else:
            cards.append(command[1])
            print("Card successfully added")
    elif command[0] == "Remove":
        if command[1] in cards:
            cards.remove(command[1])
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        if int(command[1]) >= len(cards):
            print("Index out of range")
        else:
            del cards[int(command[1])]
            print("Card successfully removed")
    elif command[0] == "Insert":
        if command[2] in cards and 0 <= int(command[1]) < len(cards):
            print("Card is already added")
        elif 0 <= int(command[1]) < len(cards):
            cards.insert(int(command[1]), command[2])
            print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(cards))