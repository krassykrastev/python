# Every gamer knows what rage-quitting means. It's when you're just not good enough, and you blame everybody else for
# losing a game - you press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.
# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something
# truly spectacular. He asks for your help.
# He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N),
# e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console.
# In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format:
# "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for
# each string, there will be a corresponding number. The input will be given on a single line.
# Input
# • The input data should be read from the console.
# • It consists of a single line holding a series of string-number sequences.
# • The input data will always be valid. There is no need to check it explicitly.
# Output
# • The output should be printed on the console. It should consist of exactly two lines:
#   o On the first line, print the number of unique symbols used in the message in the format described above.
#   o On the second line, print the rage message.
#
# Input1: a3
# Output1:
# Unique symbols used: 1
# AAA
#
# Input2: aSd2&5s@1
# Output2:
# Unique symbols used: 5
# ASDASD&&&&&S@

unique_symbols = ""
repetitions = ""
current_symbol = ""

text = input().upper()

for index in range(len(text)):

    if not text[index].isdigit():
        current_symbol += text[index]

    else: # text[index] is digit -> working with repetitions
        for next_symbols_index in range(index, len(text)):
            if not text[next_symbols_index].isdigit():
                break
            repetitions += text[next_symbols_index]
        unique_symbols += current_symbol * int(repetitions)
        repetitions = ""
        current_symbol = ""

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)