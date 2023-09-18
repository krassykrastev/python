# You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers.
# On the following line, you will be given an integer representing the capacity for one rack in your store.
# You must arrange the clothes in the store and use the racks to hang up every piece of clothing.
# You start from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose.
# Each piece of clothing has its value (an integer). You must sum their values while you take them out of the box:
# •	If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there are any left in the box).
# •	If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack and then hang it up.
# In the end, print how many racks you have used to hang up the clothes.
# Input
# •	On the first line, you will be given a sequence of integers representing the clothes in the box, separated by a single space.
# •	On the second line, you will be given an integer representing the capacity of a rack.
# Output
# •	Print the number of racks needed to hang up the clothes from the box.
# Input1:
# 5 4 8 6 3 8 7 7 9
# 16
#
# Output1: 5
#
# Input2:
# 1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20
#


clothes = input().split()
capacity_of_racks = int(input())
clothes_on_rack = 0
number_of_racks = 1

while clothes:
    current_clothes = int(clothes[-1])

    if clothes_on_rack + current_clothes > capacity_of_racks:
        number_of_racks += 1
        clothes_on_rack = int(clothes.pop())

    elif clothes_on_rack + current_clothes == capacity_of_racks:
        clothes_on_rack = 0
        clothes.pop()

        if clothes:
            number_of_racks += 1

    else:
        clothes_on_rack += int(clothes.pop())

print(number_of_racks)
