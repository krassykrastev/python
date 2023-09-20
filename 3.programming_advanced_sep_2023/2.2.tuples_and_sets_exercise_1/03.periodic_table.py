# Write a program that keeps all the unique chemical elements. On the first line, you will be given a number n - the
# count of input lines that you will receive. On the following n lines, you will be receiving chemical compounds
# separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter):
#
# Input1:
# 4
# Ce O
# Mo O Ce
# Ee
# Mo
#
# Output1:
# Ce
# Ee
# Mo
# O
#
# Input2:
# 3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne
#
# Output2:
# Ch
# Ge
# Mo
# Nb
# Ne
# O
# Tc

n = int(input())
unique_elements = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        unique_elements.add(el)

for unique_element in unique_elements:
    print(unique_element)
