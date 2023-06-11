# You will be given a number. Print the largest number that can be formed from the digits of the given number.
#
# Input1: 213
# Output1: 321
#
# Input2: 7389
# Output2: 9873

num = input()
current_number = ''

for i in range(len(num)):
    current_number += str(int(num[i]))

biggest_number = sorted(current_number, reverse=True)

print(''.join(biggest_number))

# another solution from user:subtotal
# print(''.join(reversed(sorted(list(input())))))