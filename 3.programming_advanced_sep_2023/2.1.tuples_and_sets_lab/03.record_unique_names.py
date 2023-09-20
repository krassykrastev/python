# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.
# Input1:
# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey
#
# Output1:
# Alan
# Joey
# Lee
# Joe
# Peter
#
# Input2:
# 7
# Lyle
# Bruce
# Alice
# Easton
# Shawn
# Alice
# Shawn
#
# Output2:
# Easton
# Lyle
# Alice
# Bruce
# Shawn
#
# Input3:
# 6
# Adam
# Adam
# Adam
# Adam
# Adam
# Adam
#
# Output3: Adam

n = int(input())
unique_names = set()

for i in range(n):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)
