# Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
# • Words are given on a single line, space-separated.
# • Print the result elements in lowercase, in their order of appearance.
#
# Input1: Java C# PHP PHP JAVA C java
# Output1: java c# c
#
# Input2: 3 5 5 hi pi HO Hi 5 ho 3 hi pi
# Output2: 5 hi
#
# Input3: a a A SQL xx a xx a A a XX c
# Output3: a sql xx c

dictionary = {}
sentence = input().split()

for word in sentence:
    word_lowercase = word.lower()
    if word_lowercase in dictionary:
        dictionary[word_lowercase] += 1
    else:
        dictionary[word_lowercase] = 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end = " ")