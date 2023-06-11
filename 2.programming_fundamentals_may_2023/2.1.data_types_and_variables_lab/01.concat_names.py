# Write a program that reads two names and a delimiter. It should print the names joined by the delimiter.
#
# Input1:
# John
# Smith
# ->
#
# Output1: John->Smith
#
# Input2:
# Jan
# White
# <->
#
# Output2: Jan<->White
#
# Input3:
# Linda
# Terry
# =>
#
# Output3: Linda=>Terry

first_name = input()
last_name = input()
delimiter = input()

print(f'{first_name}{delimiter}{last_name}')
