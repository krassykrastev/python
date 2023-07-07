# Create a program that receives two strings on a single line separated by a single space. Then, it prints the sum of their
# multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum, then continue
# with the next two characters. If one of the strings is longer than the other, add the remaining character codes to the
# total sum without multiplication.
#
# Input1: George Peter
# Output1: 52114
#
# Input2: 123 522
# Output2: 7647
#
# Input3: a aaaa
# Output3: 9700

total_sum = 0

first_string, second_string = input().split()

if len(first_string) > len(second_string):

    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])

elif len(second_string) > len(first_string):

    for index in range(len(first_string)):
        total_sum += ord(second_string[index]) * ord(first_string[index])

    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])

else: # len(second_string) = len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(second_string[index]) * ord(first_string[index])

print(total_sum)