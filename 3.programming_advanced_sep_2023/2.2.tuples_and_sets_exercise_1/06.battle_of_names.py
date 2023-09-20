# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values of
# each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result to a
# set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ".
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set
#
# Input1:
# 4
# Pesho
# Stefan
# Stamat
# Gosho
#
# Output1:
# 304, 128, 206, 511
#
# Input2:
# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan
#
# Output2:
# 733, 101

n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name_sum = sum([ord(char) for char in input()]) // i
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
elif sum(even_set) > sum(odd_set):
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=", ")
