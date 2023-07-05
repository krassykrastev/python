# Write a program that receives a text and a string of banned words, separated by a comma and space ", ".
# All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.
#
# Input1:
# Linux, Windows
# It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client
#
# Output1:
# It is not *****, it is GNU/*****. ***** is merely the kernel, while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/*****! Sincerely, a ******* client

banned_words = input().split(", ")
text_string = input()

for word in banned_words:
    while word in text_string:
        text_string = text_string.replace(word, len(word)*"*")

print(text_string)