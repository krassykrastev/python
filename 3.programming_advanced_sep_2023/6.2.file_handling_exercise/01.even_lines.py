# Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you
# print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
#
# text.txt:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.
#
# Output:
# fault@ his wasn't it but him@ judge to quick was @I
# safer@ is It here@ hide @Quick@

with open("text.txt", "r") as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for char in "-,.!?":
                line = line.replace(char, "@")
            print(" ".join(reversed(line.split())))
            