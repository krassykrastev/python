# You are provided with the following code. This code raises many exceptions. Fix it, so it works correctly.
# It is given a sequence of numbers, separated by a ", ". Iterate through each number by its index, and if the number is
# smaller or equal to 5, make a multiplication. If the number is larger than 5 and smaller or equal to 10, divide the
# result by the number. In the end, print the final result.
#
# Input1:
# 2, 5, 10
#
# Output1:
# 1.0
#
# Input2:
# 4, 5, 6, 1, 3
#
# Output2:
# 10.0
#
# Input3:
# 1, 4, 5
#
# Output3:
# 20.0
#
# Input4:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#
# Output4:
# 0.003968253968253968

numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
