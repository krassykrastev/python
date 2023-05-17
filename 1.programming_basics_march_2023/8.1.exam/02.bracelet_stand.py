daily_money = float(input())
daily_money_from_sales = float(input())
expenses = float(input())
gift_price = float(input())

total_money = (daily_money * 5) + (daily_money_from_sales * 5) - expenses

if total_money >= gift_price:
    print(f'Profit: {total_money:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {gift_price - total_money:.2f} BGN.')
