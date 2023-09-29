# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The
# command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the
# function in the judge system.
#
# Input1:
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
#
# Output1:
# [2, 4, 6]
#
# Input2:
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
#
# Output2:
# [1, 3, 5, 7, 9]

def even_odd(*args):
    if args[-1] == "even":
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
    elif args[-1] == "odd":
        return list(filter(lambda x: x % 2 != 0, args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print()
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
