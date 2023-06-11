# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive one of the following:
# • Opening bracket – "(",
# • Closing bracket – ")" or
# • Random string
# Your task is to find out if the brackets are balanced. That means after every opening bracket should follow a closing one.
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced.
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
#
# Input1:
# 8
# (
# 5 + 10
# )
# * 2 +
# (
# 5
# )
# -12
# Output1: BALANCED
#
# Input2:
# 6
# 12 *
# )
# 10 + 2 -
# (
# 5 + 10
# )
#
# Output2: UNBALANCED

opening_bracket = False
closing_bracket = False
balanced = True
previous_character = ''
number_of_lines = int(input())
for i in range (number_of_lines):
    current_character = input()
    if current_character == ')' and not opening_bracket:
        balanced = False
    if current_character == '(':
        opening_bracket = True
    if opening_bracket and current_character == ')':
        closing_bracket = True
    if current_character == ')' and previous_character == ')':
        balanced = False
    if current_character == '(' and previous_character == '(':
        balanced = False
    previous_character = current_character
if opening_bracket and closing_bracket and balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

# another solution from ceo
# number = int(input())
# counter = 0
# for _ in range(number):
#     check = input()
#     if "(" in check:
#         counter += 1
#     elif ")" in check:
#         counter -= 1
#     if 0 != counter != 1:
#         print("UNBALANCED")
#         break
# else:
#     print("BALANCED")