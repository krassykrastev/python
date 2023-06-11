# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically
#
# Input1: 3
#
# Output1:
# aaa
# aab
# aac
# aba
# abb
# abc
# aca
# acb
# acc
# baa
# bab
# bac
# bba
# bbb
# bbc
# bca
# bcb
# bcc
# caa
# cab
# cac
# cba
# cbb
# cbc
# cca
# ccb
# ccc
#
# Input2: 2
#
# Output2:
# aaa
# aab
# aba
# abb
# baa
# bab
# bba
# bbb

number_of_symbols = int(input())
for first_symbol in range(number_of_symbols):
    for second_symbol in range(number_of_symbols):
        for third_symbol in range(number_of_symbols):
            print(f'{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}')