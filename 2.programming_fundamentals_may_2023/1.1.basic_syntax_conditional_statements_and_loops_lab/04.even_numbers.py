# Write a program that receives a number n on the first line.
# On the following n lines, it receives different integer numbers.
# If the program receives an odd number, print "{num} is odd!" and end the program.
# Otherwise, if all numbers given are even, print "All numbers are even.".
#
# Input1:
# 2
# 12
# 286
#
# Output1: All numbers are even.
#
# Input2:
# 5
# 2
# 9
#
# Output2:
# 9 is odd

n = int(input())

for i in range(n):
    number = int(input())

    if number % 2 != 0:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')
