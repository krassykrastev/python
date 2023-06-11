# You will be given number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters:
# comma ",", period ".", or underscore "_":
# • If a string is pure, print "{string} is pure."
# • Otherwise, print "{string} is not pure!"
#
# Input1:
# 2
# pure string
# not_pure_string
#
# Output2:
# pure string is pure.
# not_pure_string is not pure!
#
# Input2:
# 3
# SoftUni
# 12345
# string.pureness
#
# Output2:
# SoftUni is pure.
# 12345 is pure.
# string.pureness is not pure!

number_n = int(input())

for i in range (number_n):
    current_string = input()
    pure_string = True
    for j in current_string:
        if j == ',' or j == '_' or j == '.':
            pure_string = False
    if pure_string:
        print(f'{current_string} is pure.')
    else:
        print(f'{current_string} is not pure!')
