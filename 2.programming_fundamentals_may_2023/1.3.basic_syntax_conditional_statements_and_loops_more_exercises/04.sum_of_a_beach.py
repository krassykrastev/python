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