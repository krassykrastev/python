# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
#
# Input1: There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
# Output1:
# :P
# :O
# :)

single_string = input()

for index in range(len(single_string)):
    if single_string[index] == ":":
        print(f"{single_string[index]}{single_string[index + 1]}")