# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the
# positive. Find the total sum of the negatives and positives, and print the following:
# •	On the first line, print the sum of the negatives
# •	On the second line, print the sum of the positives
# •	On the third line:
#   o	If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
#   o	If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.
#
# Input1:
# 1 2 -3 -4 65 -98 12 57 -84
#
# Output1:
# -189
# 137
# The negatives are stronger than the positives
#
# Input2:
# 1 2 3
#
# Output2:
# 0
# 6
# The positives are stronger than the negatives

def nums_sums(*args):
    neg_sum = 0
    pos_sum = 0
    for num in args:
        if num > 0:
            pos_sum += num
        else:
            neg_sum += num
    return neg_sum, pos_sum


nums = [int(x) for x in input().split()]

print(nums_sums(*nums)[0])
print(nums_sums(*nums)[1])

if abs(nums_sums(*nums)[0]) > nums_sums(*nums)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
