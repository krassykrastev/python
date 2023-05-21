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