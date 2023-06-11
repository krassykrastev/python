# Write a program that receives three whole numbers and prints the largest one.
#
# Input1:
# 3
# -1
# 5
#
# Output1: 5
#
# Input2:
# 0
# -1
# -2
#
# Output2: 0

num1 = int(input())
num2 = int(input())
num3 = int(input())
largest = 0

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(largest)

#num1, num2, num3 = int(input()), int(input()), int(input())
#print(max(num1,num2, num3))