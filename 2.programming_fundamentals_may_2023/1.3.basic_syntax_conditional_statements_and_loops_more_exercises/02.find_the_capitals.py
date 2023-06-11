# Write a program that takes a single string and prints a list of all the capital letters indices.
#
# Input1: pYtHoN
# Output1: [1, 3, 5]
#
# Input2: CApiTAls
# Output2: [0, 1, 4, 5]

capital_letters_indices = []
text = input()

for i in range(len(text)):
    current_letter = ord(text[i])
    if 65 <= current_letter <= 90:
        capital_letters_indices.append(i)

print(capital_letters_indices)

# another solution from user:subtotal
# word = input()
# print([x for x in range(len(word)) if word[x].isupper()])