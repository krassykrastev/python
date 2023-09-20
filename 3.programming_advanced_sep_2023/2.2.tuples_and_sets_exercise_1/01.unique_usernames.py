# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones.
# On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the
# collection on the console (the order does not matter):
#
# Input1:
# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234
#
# Output1:
# George
# Peter
# NiceGuy1234
#
# Input2:
# 10
# Peter
# Maria
# Peter
# George
# Steve
# Maria
# Alex
# Peter
# Steve
# George
#
# Output2:
# Peter
# Maria
# George
# Steve
# Alex

n = int(input())
names = set()

for _ in range(n):
    names.add(input())

for name in names:
    print(name)
# print(*names, sep="\n")
