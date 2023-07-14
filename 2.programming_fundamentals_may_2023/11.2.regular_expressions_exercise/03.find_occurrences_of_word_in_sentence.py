# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.
#
# Input1:
# The waterfall was so high, that the child couldn't see its peak.
# the
#
# Output1: 2
#
# Input2:
# How do you plan on achieving that? How? How can you even think of that?
# how
#
# Output2: 3
#
# Input3:
# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there
#
# Output3: 1

import re

sentence = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"
matches = re.findall(pattern, sentence, re.IGNORECASE)

print(len(matches))
