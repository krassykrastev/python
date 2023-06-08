# You are fed up with changing the version of your software manually. Instead, you will create a little script that will make it for you.
# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is to print the next version.
# For example, if the current version is "1.3.4", the next version will be "1.3.5".
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number.
# For more clarification, see the examples below.
# Note: there will be no case in which the first number will become greater than 9.
#
# Input1: 1.2.3
# Output1: 1.2.4
#
# Input2: 1.3.9
# Output2: 1.4.0
#
# Input3: 3.9.9
# Output3: 4.0.0

version = int(input().replace('.',''))
new_version = version + 1
print('.'.join(str(new_version)))

# another solution
# version = [int(number) for number in input().split('.')]
# version[-1] += 1
# for index in range(len(version) - 1, -1, -1):
#     if version[index] > 9 and index != 0:
#         version[index] = 0
#         if index-1 >= 0:
#             version[index-1] += 1
#
# print('.'.join(str(number) for number in version))