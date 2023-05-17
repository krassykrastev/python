capital_letters_indices = []
text = input()

for i in range(len(text)):
    current_letter = ord(text[i])
    if 65 <= current_letter <= 90:
        capital_letters_indices.append(i)

print(capital_letters_indices)
