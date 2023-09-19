# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries.
# Each query is one of these four types:
# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"
#
# Input1:
# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4
#
# Output1:
# 26
# 20
# 91, 20, 26
#
# Input2:
# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4
#
# Output2:
# 32
# 66
# 8
# 8, 16, 25, 32, 66, 47

number_of_lines = int(input())
stack_query = []

for i in range(number_of_lines):
    command = input().split()

    if command[0] == "1":
        stack_query.append(int(command[1]))

    elif command[0] == "2":
        if stack_query:
            stack_query.pop()

    elif command[0] == "3":
        if stack_query:
            print(max(stack_query))

    elif command[0] == "4":
        if stack_query:
            print(min(stack_query))

while len(stack_query) > 1:
    print(stack_query.pop(), end=", ")

print(stack_query.pop())
