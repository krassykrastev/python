# You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number
# in the format "{number} - {count} times". The number must be formatted to the first decimal point.
#
# Input1: -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# Output1:
# -2.5 - 3 times
# 4.0 - 2 times
# 3.0 - 4 times
# -5.5 - 1 times
#
# Input2: 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
# Output2:
# 2.0 - 3 times
# 4.0 - 6 times
# 5.0 - 4 times
# 3.0 - 7 times

nums = tuple(map(float, input().split()))
occ = {}

for num in nums:
    if num not in occ:
        occ[num] = nums.count(num)
        print(f"{num} - {nums.count(num)} times")
