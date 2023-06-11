# Write a program that receives a single word, reverses it, and prints it.
#
# Input1: Python
# Output1: nohtyP
#
# Input2: banana
# Output2: ananab

word = input()

for i in range(len(word) - 1, -1, -1):
    print(word[i], end='')

# print(word[::-1])
