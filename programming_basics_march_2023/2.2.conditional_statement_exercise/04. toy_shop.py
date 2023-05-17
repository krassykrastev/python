trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

order_sum = number_of_puzzles * 2.60 + number_of_dolls * 3 + number_of_bears * 4.10 + number_of_minions * 8.20 + number_of_trucks * 2

number_of_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks

if number_of_toys >= 50:
    order_sum *= 0.75 # прави се 25% отстъпка, т.е. променливата е 0.75 от цялата стойност
    # изписване е order_sum = order_sum * 0.75

rent = order_sum * 0.1

profit = order_sum - rent
diff = abs(profit - trip_price)

if profit >= trip_price:
    print(f'Yes! {diff:.2f} lv left.')

else:
    print(f'Not enough money! {diff:.2f} lv needed.')
