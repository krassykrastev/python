# Trifon has finally become a junior developer and has received his first task. It is about manipulating a list of integers.
# He is not quite happy about it since he hates manipulating lists.
# They will pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job.
# On the other hand, you love lists (and money), so you decide to try your luck.
# The list may be manipulated by one of the following commands:
# • "exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists.
#    E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
#    o If the index is outside the boundaries of the list, print "Invalid index"
#    o A negative index is considered invalid
# • "max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
# • "min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
#    o If there are two or more equal min/max elements, return the index of the rightmost one
#    o If a min/max even/odd element cannot be found, print "No matches"
# • "first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
# • "last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
#    o If the count is greater than the list length, print "Invalid count"
#    o If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty list "[]"
# • "end" - stop taking input and print the final state of the list
#
# Input1:
# 1 3 5 7 9
# exchange 1
# max odd
# min even
# first 2 odd
# last 2 even
# exchange 3
# end
#
# Output1:
# 2
# No matches
# [5, 7]
# []
# [3, 5, 7, 9, 1]
#
# Input2:
# 1 10 100 1000
# max even
# first 5 even
# exchange 10
# min odd
# exchange 0
# max even
# min even
# end
#
# Output2:
# 3
# Invalid count
# Invalid index
# 0
# 2
# 0
# [10, 100, 1000, 1]
#
# Input3:
# 1 10 100 1000
# exchange 3
# first 2 odd
# last 4 odd
# end
#
# Output3:
# [1]
# [1]
# [1, 10, 100, 1000]

#solution by ceo as I was not able to find solution on my own
numbers = [int(i) for i in input().split()]
command = input().split()

while command[0] != "end":
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')

    elif command[0] == "max":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(max(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(max(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(min(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(min(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[0:int(command[1])])
            else:
                print(odd[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[-int(command[1]):])
            else:
                print(odd[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()

print(numbers)