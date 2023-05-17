money_needed = float(input())
money_owned = float(input())

spend_counter = 0
days_counter = 0

while True:
    days_counter += 1
    action = input()
    current_money = float(input())

    if action == 'spend':
        spend_counter += 1
        money_owned -= current_money
        if money_owned < 0:
            money_owned = 0
    elif action == 'save':
        spend_counter = 0
        money_owned += current_money

    if money_owned >= money_needed:
        print(f'You saved the money for {days_counter} days.')
        break
    elif spend_counter == 5:
        print("You can't save the money.")
        print(days_counter)
        break
