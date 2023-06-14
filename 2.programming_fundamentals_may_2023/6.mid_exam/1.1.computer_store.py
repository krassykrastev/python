# Write a program that prints you a receipt for your new computer.
# You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular.
# Once you receive the type of customer you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next price.
# If the total price is equal to zero, you should print "Invalid order!" on the console.
#
# Input1:
# 1050
# 200
# 450
# 2
# 18.50
# 16.86
# special
#
# Output1:
# Congratulations you've just bought a new computer!
# Price without taxes: 1737.36$
# Taxes: 347.47$
# -----------
# Total price: 1876.35$
#
# Input2:
# 1023
# 15
# -20
# -5.50
# 450
# 20
# 17.66
# 19.30
# regular
#
# Output2:
# Invalid price!
# Invalid price!
# Congratulations you've just bought a new computer!
# Price without taxes: 1544.96$
# Taxes: 308.99$
# -----------
# Total price: 1853.95$
#
# Input3: regular
# Output3: Invalid order!

price_adjustment = 1 # price for regular customer

total_sum = 0
part_price_or_customer_type = input()

while part_price_or_customer_type != "special" and part_price_or_customer_type != "regular":
    part_price = float(part_price_or_customer_type)

    if part_price > 0:
        total_sum += part_price
    else:
        print("Invalid price!")

    part_price_or_customer_type = input()

taxes = total_sum * 0.2

if part_price_or_customer_type == "special":
    price_adjustment = 0.9

if total_sum == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {(total_sum + taxes) * price_adjustment:.2f}$")