# Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and
# unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you have been
# tasked to analyze the software of the virus and observe its actions on the data.
# You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII character except whitespace.
# Then you will begin receiving commands in one of the following formats:
# • merge {startIndex} {endIndex}
# • divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex.
# In other words, you should concatenate them. Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index into several small substrings with equal length.
# The count of the substrings should be equal to the given partitions. Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.
#
# Input1:
# Ivo Johny Tony Bony Mony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1
#
# Output1: IvoJohnyTonyBonyMony
#
# Input2:
# abcd efgh ijkl mnop qrst uvwx yz
# merge 4 10
# divide 4 5
# 3:1
#
# Output2: abcd efgh ijkl mnop qr st uv wx yz

output_string = []
def merge(start_index, end_index):
    if start_index < 0:
        start_index = 0
    if start_index < end_index:
        how_long = len(line_of_strings)
        if end_index >= how_long:
            end_index = how_long - 1
        for num in range(start_index, end_index):
            line_of_strings[start_index] += f"{line_of_strings.pop(start_index + 1)}"

def divide(index, partitions):
    how_long = len(line_of_strings[index])
    space_between = how_long // partitions
    string_to_change = line_of_strings.pop(index)
    result_ = []
    for x in range(partitions - 1):
        result_.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result_.append(string_to_change)
    for x in result_[::-1]:
        line_of_strings.insert(index, x)

line_of_strings = input().split(' ')
command = input().split(' ')

while command[0] != '3:1':
    if command[0] == 'merge':
        index_start = int(command[1])
        index_end = int(command[2])
        merge(index_start, index_end)
    elif command[0] == 'divide':
        index_ = int(command[1])
        partition = int(command[2])
        divide(index_, partition)
    command = input().split(' ')

print(' '.join(line_of_strings))