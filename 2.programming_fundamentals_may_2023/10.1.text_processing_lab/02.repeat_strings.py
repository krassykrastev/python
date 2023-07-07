# Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N times,
# where N is the length of the string. Print the final strings concatenated into one string.
#
# Input1: hi abc add
# Output1: hihiabcabcabcaddaddadd
#
# Input2: work
# Output2: workworkworkwork
#
# Input3: ball
# Output3: ballballballball

final_string = ""

text_string = input().split()

for word in text_string:
    final_string += word * len(word)

print(final_string)