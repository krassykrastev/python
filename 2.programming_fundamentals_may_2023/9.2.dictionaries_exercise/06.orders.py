# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
# • If the product doesn't exist yet, add it with its starting quantity.
# • If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different,
# replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
# • Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# • The product data is always delimited by a single space.
# Output
# • Print information about each product in the following format: "{product_name} -> {total_price}"
# • Format the total price to the 2nd digit after the decimal separator.
#
# Input1:
# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy
#
# Output1:
# Beer -> 220.00
# IceTea -> 75.00
# NukaCola -> 264.00
# Water -> 500.00
#
# Input2:
# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy
#
# Input3:
# CesarSalad 10.20 25
# SuperEnergy 0.80 400
# Beer 1.35 350
# IceCream 1.50 25
# buy
#
# Output3:
# CesarSalad -> 255.00
# SuperEnergy -> 320.00
# Beer -> 472.50
# IceCream -> 37.50

products = {}

command = input().split()

while command[0] != "buy":
    product_name, price, quantity = command[0], float(command[1]), int(command[2])
    if product_name not in products.keys():
        products[product_name] = [price, quantity]
    else:
        products[product_name][0] = price
        products[product_name][1] += quantity
    command = input().split()

for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")