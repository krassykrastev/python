# Write a program that finds all integer and floating-point numbers in a string.
# Compose the Regular Expression
# A number has the following characteristics:
# • Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind).
# The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
# • The number might or might not be negative, so it might have a hyphen on its left side ("-").
# • It consists of one or more digits.
# • Might or might not have digits after the decimal point
# • The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
# • Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead).
# The syntax for the end of the RegEx might look something like "($|(?=\s))".
#
# Input1: 1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5
# Output1: 1 -1 123 -123 123.456 -123.456

import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

string = input()

matches = re.finditer(pattern, string)

for match in matches:
    print(match.group(), end=" ")