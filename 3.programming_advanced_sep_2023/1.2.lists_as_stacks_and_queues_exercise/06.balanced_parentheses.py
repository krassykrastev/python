# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs
# after the former. There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
# •	On a single line, you will receive a sequence of parentheses.
# Output
# •	For each test case, print on a new line "YES" if the parentheses are balanced.
# •	Otherwise, print "NO"
#
# Input1: {[()]}
# Output1: YES
#
# Input2: {[(])}
# Output2: NO
#
# Input3: {{[[(())]]}}
# Output3: YES

from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    left_parentheses = parentheses.popleft()

    if left_parentheses in "{([":
        open_parentheses.append(left_parentheses)

    elif not open_parentheses:
        print("NO")
        break

    else:
        if f"{open_parentheses.pop() + left_parentheses}" not in "{}()[]":
            print("NO")
            break

else:
    print("YES")

# parentheses = input()
# opening_parentheses = []
#
# is_balanced = True
#
# for parent in parentheses:
#     if parent in "[{(":
#         opening_parentheses.append(parent)
#
#     else:
#         if opening_parentheses:
#             current_parentheses = opening_parentheses.pop() + parent
#
#             if current_parentheses not in ["{}", "()", "[]"]:
#                 is_balanced = False
#
#         else:
#             is_balanced = False
#
#     if not is_balanced:
#         break
#
# print("YES") if is_balanced else print("NO")