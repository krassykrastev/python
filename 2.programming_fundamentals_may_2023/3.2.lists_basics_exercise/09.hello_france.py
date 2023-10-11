# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide
# to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:

# Type              Maximum Price
# Clothes           50.00
# Shoes             35.00
# Accessories       20.50
#
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item,
# you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it.
# Calculate if the budget after selling all the items is enough for buying the train ticket.
#
# Input1:
# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120
#
# Output1:
# 60.62 35.35 51.13
# Profit: 42.03.core
# Hello, France!
#
# Input2:
# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90
#
# Output2:
# 28.42 21.84 46.62
# Profit: 27.68
# Not enough money.

items = input().split('|')
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150

for item in items:
    type, buying_price = item.split('->')
    buying_price = float(buying_price)
    price_is_valid = False
    if type == 'Clothes':
        if buying_price <= 50.00:
            price_is_valid = True
    elif type == 'Shoes':
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == 'Accessories':
        if buying_price <= 20.50:
            price_is_valid = True
    if price_is_valid:
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.40
            profit += sell_price - buying_price
            sell_prices.append(sell_price)

for sell_price in sell_prices:
    print(f'{sell_price:.2f}', end = ' ')
print()
# option 2
# print(' '.join([f'{sell_price:.2f}' for sell_price in sell_prices]))

# option 3
# sell_prices_as_string = []
# for sell_price in sell_prices:
#     sell_prices_as_string.append(f'{sell_price:.2f}')
# print(' '.join(sell_prices_as_string))

print(f'Profit: {profit:.2f}')
total_income = budget + sum(sell_prices)
if total_income >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')