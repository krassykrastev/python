# You work at a coffee shop, and your job is to place orders to the distributors.
# Thus, you want to know the price of each order.
# On the first line, you will receive integer N - the number of orders the shop will receive.
# For each order, you will receive the following information:
# • Price per capsule - a floating-point number in the range [0.01…100.00]
# • Days - integer in the range [1…31]
# • Capsules, needed per day - integer in the range [1…2000]
# For each order, you should print a single line in the following format:
# • "The price for the coffee is: ${price}"
# If you do not receive a correct order (one or more of the values are not in the given range), you should ignore it and move to the next one.
# After you go through all orders, you need to print the total price in the following format:
# • "Total: ${total_price}"
# Both the price of a coffee and the total price must be formatted to the second decimal place.
#
# Input1:
# 1
# 1.53
# 30
# 8
#
# Output1:
# The price for the coffee is: $367.20
# Total: $367.20
#
# Input2:
# 2
# 4.99
# 31
# 3
# 0.35
# 31
# 5
#
# Output2:
# The price for the coffee is: $464.07 The price for the coffee is: $54.25
# Total: $518.32
#
# Input3:
# 2
# 9.223
# 31
# 0
# 0.05
# 10
# 30
#
# Output3:
# The price for the coffee is: $15.00
# Total: $15.00

number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    amount_of_capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif amount_of_capsules_per_day < 1 or amount_of_capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * amount_of_capsules_per_day
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total_price:.2f}')
