# On the first line, you will receive a number n. On the second line, you will receive a word.
# On the following n lines, you will be given some strings. You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.
#
# Input1:
# 3
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni
#
# Output1:
# ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
# ["I study at SoftUni", "I learn Python at SoftUni"]
#
# Input2:
# 4
# tomatoes
# I love tomatoes
# I can eat tomatoes forever
# I don't like apples
# Yesterday I ate two tomatoes
#
# Output2:
# ["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]
# ["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"]

n = int(input())
special_word = input()

strings = []

for i in range(n):
    string = input()
    strings.append(string)

print(strings)

filtered_strings= []

for string in strings:
    if special_word in string:
        filtered_strings.append(string)

print(filtered_strings)