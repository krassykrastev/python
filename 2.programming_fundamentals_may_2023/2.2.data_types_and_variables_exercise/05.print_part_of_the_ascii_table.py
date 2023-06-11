# Write a program that prints part of the ASCII table characters on the console, separated by a single space.
# On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.
#
# Input1:
# 60
# 65
#
# Output1: < = > ? @ A
#
# Input2:
# 69
# 79
#
# Output2: E F G H I J K L M N O
#
# Input3:
# 97
# 104
#
# Output3: a b c d e f g h

start_index = int(input())
final_index = int(input())
for character in range(start_index, final_index + 1):
    print(chr(character), end=' ')