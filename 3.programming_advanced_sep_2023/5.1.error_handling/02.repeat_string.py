# Write a program that receives a text on the first line and times (to repeat the text) that must be an integer. If the
# user passes a non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".
#
# Input1:
# Hello
# Bye
#
# Output1:
# Variable times must be an integer
#
# Input2:
# Hello
# 2
#
# Output2:
# HelloHello

word = input()

try:
    times = int(input())

except ValueError:
    print("Variable times must be an integer")

else:
    print(word*times)
