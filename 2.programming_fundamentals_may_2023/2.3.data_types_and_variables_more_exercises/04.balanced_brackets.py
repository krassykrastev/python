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

# another solution from raya
# n = int(input())
# example = ""
# not_balanced = False
#
# for i in range(1, n + 1):
#     text = input()
#     if text != "(" and text != ")":
#         continue
#     if text == "(" and example == "":
#         example += "("
#     elif text == ")" and example == "(":
#         example = ""
#     else:
#         not_balanced = True
#         break
#
# if not not_balanced:
#     print("BALANCED")
# else:
#     print("UNBALANCED")