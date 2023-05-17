savings = 0
current_savings = 0

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    while True:
        current_savings = float(input())
        savings += current_savings
        if savings >= budget:
            savings = 0
            break
    if destination != "End":
        print(f'Going to {destination}!')
