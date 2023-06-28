# Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word. The value will
# be a list of all the synonyms of that word. You will be given a number n – the count of the words. After each term,
# you will be given a synonym, so the count of lines you should read from the console is 2 * n. You will be receiving a
# word and a synonym each on a separate line like this:
# • {word}
# • {synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2 … synonymN}
#
# Input1:
# 3
# cute
# adorable
# cute
# charming
# smart
# clever
#
# Output1:
# cute - adorable, charming
# smart - clever
#
# Input2:
# 2
# task
# problem
# task
# assignment
#
# Output2:
# task – problem, assignment

n = int(input())
synonyms = {}

for i in range (n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym_list in synonyms.items():
    synonyms_str = ', '.join(synonym_list)
    print(f"{word} - {synonyms_str}")