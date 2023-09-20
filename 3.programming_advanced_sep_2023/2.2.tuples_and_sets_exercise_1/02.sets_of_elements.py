# Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, separated
# by a single space - representing the lengths of two separate sets. On the next n + m lines, you will receive n numbers,
# which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that
# appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}
#
# Input1:
# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5
#
# Output1:
# 3
# 5
#
# Input2:
# 2 2
# 1
# 3
# 1
# 5
#
# Output2:
# 1

n, m = input().split()

n_set = set()
m_set = set()

for _ in range(int(n)):
    n_set.add(input())

for _ in range(int(m)):
    m_set.add(input())

common_elements = n_set.intersection(m_set)  # n_set & m_set

for common_element in common_elements:
    print(common_element)
