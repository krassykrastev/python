# Create a program, that checks if inputs have a valid message and encrypt it.
# On the first line you will receive a number that indicates how many inputs you will receive on the next lines.
# A message is valid when:
# -	It is in the end of the input
# -	It starts with a tag, which is surrounded by either '*' or '@' (but not both at the same time),
# the tag itself has to be minimum 3 characters long, start with a uppercase letter, followed only by lowercase letters
# -	There is a colon and a single white space after the tag
# -	There are 3 groups consisting of letters between '[' and ']', followed by a pipe ('|')
# Example for a valid message:
# "*Request*: [I]|[s]|[i]| "
# You must check if the message is valid and if it is- decrypt it, if it isn’t- print the following message:
# "Valid message not found!"
# Encrypting a message means to take all letters and turn them into ASCII numbers. After successful encrypt, print it in the following format:
# {tag}: {number1} {number2} {number3} (…)
# Input
# •	On the first line - n - the count of inputs.
# •	On the next n lines - input that you have to check if it has a valid message.
# Output
# •	Print all results from each input, each on a new line.
# Input1:
# 3
# *Request*: [I]|[s]|[i]|
# *Taggy@: [73]|[73]|[73]|
# Should be valid @Taggy@: [v]|[a]|[l]|
#
# Output1:
# Request: 73 115 105
# Valid message not found!
# Taggy: 118 97 108
#
# Input2:
# 3
# @Taggy@: [i]|[n]|[v]|[a]|[l]|[i]|[d]| this shouldn’t be valid
# *tAGged*: [i][i][i]|
# Should be invalid @Taggy@: [v]|[a]|[l]|[l]|[l]|
#
# Output2:
# Valid message not found!
# Valid message not found!
# Valid message not found!

import re
n = int(input())

for i in range(n):
    text = input()
    pattern = r"([*@])(?P<tag>[A-Z][a-z]{2,})(\1)(: \[)(?P<one>[A-Za-z])(\]\|\[)(?P<two>[A-Za-z])(\]\|\[)(?P<three>[A-Za-z])(\]\|)$"
    match = re.search(pattern, text)

    if match is None:
        print("Valid message not found!")
        continue
    tag = match.group("tag")
    first_string = match.group("one")
    second_string = match.group("two")
    third_string = match.group("three")
    print(f'{tag}: {ord(first_string)} {ord(second_string)} {ord(third_string)}')

# import re
#
# number_of_msg = int(input())
#
# pattern = re.compile(r"^([$%])(?P<tag>[A-Z][a-z]{2,})\1: "
#                      r"\[(?P<num1>[\d]+)"
#                      r"\]\|\[(?P<num2>[\d]+)"
#                      r"\]\|\[(?P<num3>[\d]+)\]\|$")
#
# for _ in range(number_of_msg):
#     msg_to_decrypt = input()
#     result = list(pattern.finditer(msg_to_decrypt))
#     for show in result:
#         successful_decrypt = f'{chr(int(show["num1"]))}{chr(int(show["num2"]))}{chr(int(show["num3"]))}'
#         print(f"{show['tag']}: {successful_decrypt}")
#     if not result:
#         print("Valid message not found!")