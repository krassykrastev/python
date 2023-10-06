# Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and
# punctuation marks. The result should be written in another text file.
#
# text2.txt
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.
#
# output2.txt:
# Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
# Line 2: -Is this some kind of joke?! Is it? (24)(4)
# Line 3: -Quick, hide here. It is safer. (22)(4)

from string import punctuation

with open("text2.txt", "r") as input_file, open("output.txt", "w") as output_file:
    result = []
    for row, line in enumerate(input_file):
        letters_count = 0
        punc_count = 0
        for char in line:
            if char.isalpha():
                letters_count += 1
            elif char in punctuation:
                punc_count += 1
        result.append(f"Line {row + 1}: {line.strip()} ({letters_count})({punc_count})")
    output_file.write("\n".join(result))
