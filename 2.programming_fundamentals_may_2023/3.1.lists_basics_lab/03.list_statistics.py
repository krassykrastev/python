# On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:
# • One with all the positives (including 0) numbers
# • One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"
#
# Input1:
# 5
# 10
# 3
# 2
# -15
# -4
#
# Output1:
# [10, 3, 2]
# [-15, -4]
# Count of positives: 3
# Sum of negatives: -19
#
# Input2:
# 6
# 11
# 2
# 35
# 599
# 31
# 20
#
# Output2:
# [11, 2, 35, 599, 31, 20]
# []
# Count of positives: 6
# Sum of negatives: 0

n = int(input())

positives = []
negatives = []

for i in range(n):
    number = int(input())

    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')