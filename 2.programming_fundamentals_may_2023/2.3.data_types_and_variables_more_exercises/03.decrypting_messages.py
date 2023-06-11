# On the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines, which will follow.
# On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message.
# In the end, print the decrypted message.
#
# Input1:
# 3
# 7
# P
# l
# c
# q
# R
# k
# f
#
# Output1: SoftUni
#
# Input2:
# 1
# 7
# C
# d
# b
# q
# x
# o
# s
#
# Output2: Decrypt

string = ''
decrypt_key = int(input())
number_of_lines = int(input())

for i in range(number_of_lines):
    current_character = input()
    string += chr(ord(current_character) + decrypt_key)

print(string)