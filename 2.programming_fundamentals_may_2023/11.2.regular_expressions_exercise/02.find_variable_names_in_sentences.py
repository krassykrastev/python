# Write a program that finds all variable names in each string.
# A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits.
# Extract only their names without the underscore. Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.
#
# Input1: The _id and _age variables are both integers.
# Output1: id,age
#
# Input2: Calculate the _area of the _perfectRectangle object.
# Output2: area,perfectRectangle
#
# Input3: __invalidVariable _evenMoreInvalidVariable_ _validVariable
# Output3: validVariable

import re

sentence = input()

pattern = r"\b_([A-Za-z0-9]+)\b"

found_variable_names = re.findall(pattern, sentence)
print(",".join(found_variable_names))
