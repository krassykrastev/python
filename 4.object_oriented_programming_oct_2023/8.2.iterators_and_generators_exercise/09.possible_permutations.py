# Create a generator function called possible_permutations() which should receive a list
# and return lists with all possible permutations between its elements.
#
# Test code1:
# [print(n) for n in possible_permutations([1, 2, 3])]
#
# Output1:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
#
# Test code2:
# [print(n) for n in possible_permutations([1])]
#
# Output2:
# [1]

def possible_permutations(ls):
    if len(ls) <= 1:
        yield ls
    else:
        for i in range(len(ls)):
            for perm in possible_permutations(ls[:i] + ls[i + 1:]):
                yield [ls[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]

print()

[print(n) for n in possible_permutations([1])]
