# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.
#
# Input1:
# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45
#
# Output1: 300 3 22 45
#
# Input2:
# 123a456
# 789b987
# 654c321
# 0
#
# Output2: 123 456 789 987 654 321 0
#
# Input3:
# Let's go11!!!11!
# Okey!1!
#
# Output3: 11 11 1

import re

line = input()

while line:
    pattern = "\d+"

    matches = re.findall(pattern, line)

    if matches:
        print(" ".join(matches), end=" ")

    line = input()