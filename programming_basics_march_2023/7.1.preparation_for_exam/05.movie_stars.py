budget = float(input())

while True:
    command = input()

    if command == 'ACTION' or budget <= 0:
        break

    actor_name = command

    if len(actor_name) <= 15:
        actor_fee = float(input())
    else:
        actor_fee = budget * 0.20

    budget -= actor_fee

if budget >= 0:
    print(f'We are left with {budget:.2f} leva.')
else:
    print(f'We need {abs(budget):.2f} leva for our actors.')
