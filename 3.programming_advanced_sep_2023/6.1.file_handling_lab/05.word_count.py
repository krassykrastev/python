# Write a program that reads a list of words from the file words.txt and finds how many times each of the words is
# contained in another file text.txt. Matching should be case-insensitive. The results should be written into other text
# files. Sort the words by frequency in descending order.
#
# words.txt:
# quick is fault
#
# input.txt:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here…It is safer.
#
# output.txt:
# is - 3
# quick - 2
# fault - 1
import re

with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()

with open("input.txt", "r") as file:
    text = file.read().lower()


words = {}
for searched_word in searched_words:
    pattern = f"\\b{searched_word}\\b"
    result = re.findall(pattern, text)
    words[searched_word] = len(result)

words_sorted = sorted(words.items(), key=lambda kvp: -kvp[1])

with open("output.txt", "w") as file:
    for key, value in words_sorted:
        file.write(f"{key} - {value}\n")
