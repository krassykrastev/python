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

expression = input()
stack = []

for index in range(len(expression)):

    if expression[index] == "(":
        stack.append(index)

    elif expression[index] == ")":
        start_index = stack.pop()
        last_index = index + 1
        print(expression[start_index:last_index])
