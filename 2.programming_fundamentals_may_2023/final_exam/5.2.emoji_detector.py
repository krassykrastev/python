# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# The cool threshold could be a huge number, so be mindful.
# An emoji is valid when:
# •	It is surrounded by 2 characters, either "::" or "**"
# •	It is at least 3 characters long (without the surrounding symbols)
# •	It starts with a capital letter
# •	Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined
# by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that to take all emojis out of the text, count them and
# print only the cool ones on the console.
#
# Input1: In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**
#
# Output1:
# Cool threshold: 540
# 4 emojis found in the text. The cool ones are:
# ::Smiley::
# **Tigers**
# ::Mooning::
#
# Input2: 5, 4, 3, 2, 1, go! The 1-th consecutive banana-eating contest has begun! ::Joy:: **Banana** ::Wink:: **Vali** ::valid_emoji::
#
# Output2:
# Cool threshold: 120
# 4 emojis found in the text. The cool ones are:
# ::Joy::
# **Banana**
# ::Wink::
# **Vali**
#
# Input3: It is a long established fact that 1 a reader will be distracted by 9 the readable content of a page when looking at its layout. The point of using ::LoremIpsum:: is that it has a more-or-less normal 3 distribution of 8 letters, as opposed to using 'Content here, content 99 here', making it look like readable **English**.
#
# Output3:
# Cool threshold: 17496
# 1 emojis found in the text. The cool ones are:

import re

data = input()
pattern = r"\d|(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2,})"
result = re.finditer(pattern, data)
words = {}
cool_threshold = 1

for res in result:
    word = res.group()

    if word.isdigit():
        cool_threshold *= int(word)

    else:
        words[word] = 0
        for ch in word:
            if ch != ":" and ch != "*":
                words[word] += ord(ch)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(words)} emojis found in the text. The cool ones are:")

for current_word in words:
    if words[current_word] >= cool_threshold:
        print(current_word)
