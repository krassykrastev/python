# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in
# the examples below.
# •	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# •	Columns + rows define the middle letter:
#   o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
#   o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
#
# Input1:
# 4 6
#
# Output1:
# aaa aba aca ada aea afa
# bbb bcb bdb beb bfb bgb
# ccc cdc cec cfc cgc chc
# ddd ded dfd dgd dhd did
#
# Input2:
# 3 2
#
# Output2:
# aaa aba
# bbb bcb
# ccc cdc

r, c = [int(x) for x in input().split()]

start = ord('a')

for row in range(r):
    for col in range(c):
        print(f"{chr(start + row)}{chr(start + row + col)}{chr(start + row)}", end=" ")
    print()
    