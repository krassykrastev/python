# You are given an algebraic expression with parentheses. Scan through the string and extract each set of
# parentheses. Print the result back on the console.
#
# Input1: 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# Output1:
# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))
#
# Input2: (2 + 3) - (2 + 3)
# (2 + 3)
# (2 + 3)

algebraic_expression = input()

indexes = []

for i in range(len(algebraic_expression)):
    current_character = algebraic_expression[i]

    if current_character == "(":
        indexes.append(i)

    elif current_character == ")":
        l = indexes.pop()
        print(algebraic_expression[l:i + 1])
