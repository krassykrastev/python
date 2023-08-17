journey_cost = float(input())
number_months = int(input())

saved_money = 0
for month in range(1, number_months + 1):
    if not month % 2 == 0 and month > 1:
        saved_money -= 0.16 * saved_money
    elif month % 4 == 0:
        saved_money += 0.25 * saved_money

    saved_money += 0.25 * journey_cost

if saved_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {(saved_money - journey_cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(journey_cost - saved_money):.2f}lv. more.")