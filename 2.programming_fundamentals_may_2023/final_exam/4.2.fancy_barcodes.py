# Your first task is to determine if the given sequence of characters is a valid barcode or not.
# Each line must not contain anything else but a valid barcode. A barcode is valid when:
# •	It is surrounded by a "@" followed by one or more "#"
# •	It is at least 6 characters long (without the surrounding "@" or "#")
# •	It starts with a capital letter
# •	It contains only letters (lower and upper case) and digits
# •	It ends with a capital letter
# Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
# Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
# Next, you have to determine the product group of the item from the barcode.
# The product group is obtained by concatenating all the digits found in the barcode.
# If there are no digits present in the barcode, the default product group is "00".
# Examples:
# @#FreshFisH@# -> product group: 00
# @###Brea0D@### -> product group: 0
# @##Che4s6E@## -> product group: 46
#
# Input1:
# 3
# @#FreshFisH@#
# @###Brea0D@###
# @##Che4s6E@##
#
# Output1:
# Product group: 00
# Product group: 0
# Product group: 46
#
# Input2:
# 6
# @###Val1d1teM@###
# @#ValidIteM@#
# ##InvaliDiteM##
# @InvalidIteM@
# @#Invalid_IteM@#
# @#ValiditeM@#
#
# Output2:
# Product group: 11
# Product group: 00
# Invalid barcode
# Invalid barcode
# Invalid barcode
# Product group: 00

import re

pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
digits_pattern = r"\d"


n = int(input())

for i in range(n):
    row_data = input()

    if re.match(pattern, row_data):
        digits = re.findall(digits_pattern, row_data)

        if digits:
            product_group = "".join(digits)

        else:
            product_group = "00"

        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
