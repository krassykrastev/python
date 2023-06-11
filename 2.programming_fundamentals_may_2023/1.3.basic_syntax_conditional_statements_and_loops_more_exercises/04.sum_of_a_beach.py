# Beaches are filled with sand, water, fish, and sun.
# Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
#
# Input1: WAtErSlIde
# Output1: 1
#
# Input2: GolDeNSanDyWateRyBeaChSuNN
# Output2: 3
#
# Input3: gOfIshsunesunFiSh
# Output3: 4
#
# Input4: cItYTowNcARShoW
# 0

count = 0

text = input().lower()
count += text.count("sand")
count += text.count("water")
count += text.count("fish")
count += text.count("sun")

print(count)

# another solution from user:subtotal
# import re
#
# word = input().lower()
# regex = r"fish|sun|sand|water"
# matches = re.findall(regex, word)
# print(len(matches))