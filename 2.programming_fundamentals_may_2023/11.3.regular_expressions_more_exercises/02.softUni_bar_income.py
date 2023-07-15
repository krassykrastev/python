# Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the
# bar to go home and you are the person who has to draw the line and calculate the money from the products
# that were sold throughout the day. Until you receive a line with text "end of shift" you will be given
# lines of input. But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# • Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by
# lower-case letters
# • Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'
# • Valid count is an integer, surrounded by '|'
# • Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places
# in the following format: "Total income: {income}".
#
# Input1:
# %George%<Croissant>|2|10.3$
# %Peter%<Gum>|1|1.3$
# %Maria%<Cola>|1|2.4$
# end of shift
#
# Output1:
# George: Croissant - 20.60
# Peter: Gum - 1.30
# Maria: Cola - 2.40
# Total income: 24.30
#
# Input2:
# %InvalidName%<Croissant>|2|10.3$
# %Peter%<Gum>1.3$
# %Maria%<Cola>|1|2.4
# %Valid%<Valid>valid|10|valid20$
# end of shift
#
# Output2:
# Valid: Valid - 200.00
# Total income: 200.00

import re

total_price = 0
pattern = "%([A-Z][a-z]+)%([^\|\$\%\.]*)<([\w]+)>([^\|\$\%\.]*)\|([\d]+)\|([^\|\$\%\.]*)([1-9]+[.0-9]*)\$"

while True:

    command = input()

    if command == "end of shift":
        break

    matches = re.findall(pattern, command)

    for match in matches:
        if match:
            customer = match[0]
            product = match[2]
            quantity = int(match[4])
            price = float(match[6])
            current_price = quantity * price
            total_price += quantity * price
            print(f"{customer}: {product} - {current_price:.2f}")

print(f"Total income: {total_price:.2f}")
