# Write a program to match full names from a sequence of characters and print them on the console.
# Writing the Regular Expression
# First, write a regular expression to match a valid full name, according to these conditions:
# • A valid full name has the following characteristics:
#   o It consists of two words.
#   o Each word starts with a capital letter.
#   o After the first letter, it only contains lowercase letters.
#   o Each of the two words should be at least two letters long.
#   o A single space separates the two words.
# To help you out, we have outlined several steps:
# 1. Use the online regex tester like https://pythex.org/
# 2. Check out how to use character sets (denoted with square brackets - "[]")
# 3. Specify that you want two words with a space between them (the space character ' ', and not any whitespace symbol)
# 4. For each word, specify that it should begin with an uppercase letter using a character set.
# The desired characters are in a range – from 'A' to 'Z'.
# 5. For each word, specify that what follows the first letter are only lowercase letters, one or more –
# use another character set and the correct quantifier.
# 6. To prevent capturing of letters across new lines, put "\b" at the beginning and at the end of your regex.
# This will ensure that what precedes and what follows the match is a word boundary (like a new line).
#
# Input1: Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett
# Output1: Peter Smith Lily Everett

import re

names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matches = re.findall(pattern, names)

for name in matches:
    print(name, end=" ")