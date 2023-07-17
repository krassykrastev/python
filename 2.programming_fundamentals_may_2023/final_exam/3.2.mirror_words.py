# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there.
# It`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that
# you are the best, so go ahead, learn the rules and win!
# On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden
# word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!),
# they are a match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
#
# Input1: @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r
# Output1:
# 5 word pairs found!
# The mirror words are:
# Part <=> traP, leveL <=> Level, sAw <=> wAs
#
# Input2: #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@
# Output2:
# 2 word pairs found!
# No mirror words!
#
# Input3: #lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#
# Output3:
# No word pairs found!
# No mirror words!

import re

mirror_words = []
word_pairs = 0

data = input()
pattern = r"([#@])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
result = re.findall(pattern, data)

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f"{pair[1]} <=> {pair[3]}")

    word_pairs += 1

if word_pairs > 0:
    print(f"{word_pairs} word pairs found!")

    if not mirror_words:
        print("No mirror words!")

    else:
        print("The mirror words are:")
        print(", ".join(mirror_words))

else:
    print("No word pairs found!")
    print("No mirror words!")
