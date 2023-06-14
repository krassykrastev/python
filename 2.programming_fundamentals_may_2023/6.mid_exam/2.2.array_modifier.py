# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# •	"swap {index1} {index2}" takes two elements and swap their places.
# •	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index.
# •	"decrease" decreases all elements in the array with 1.
# Input
# On the first input line, you will be given the initial array values separated by a single space.
# On the next lines you will receive commands until you receive the command "end". The commands are as follow:
# •	"swap {index1} {index2}"
# •	"multiply {index1} {index2}"
# •	"decrease"
# Output
# The output should be printed on the console and consist of elements of the modified array – separated by a comma and a single space ", ".
#
# Input1:
# 23 -2 321 87 42 90 -123
# swap 1 3
# swap 3 6
# swap 1 0
# multiply 1 2
# multiply 2 1
# decrease
# end
#
# Output1: 86, 7382, 2369942, -124, 41, 89, -3
#
# Input2:
# 1 2 3 4
# swap 0 1
# swap 1 2
# swap 2 3
# multiply 1 2
# decrease
# end
#
# Output2: 1, 11, 3, 0

list_of_integers = [int(x) for x in input().split(" ")]
command = input().split(" ")
while command[0] != "end":
    if command[0] == "decrease":
        list_of_integers = [x - 1 for x in list_of_integers]
        command = input().split(" ")
        continue
    if command[0] == "swap":
        list_of_integers[int(command[1])], list_of_integers[int(command[2])] = list_of_integers[int(command[2])], list_of_integers[int(command[1])]
    elif command[0] == "multiply":
        list_of_integers[int(command[1])] *= list_of_integers[int(command[2])]

    command = input().split(" ")

print(*list_of_integers, sep= ", ")