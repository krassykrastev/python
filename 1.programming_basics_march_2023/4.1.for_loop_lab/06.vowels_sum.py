input_text = input()
value = 0

for char in input_text:
    if char == 'a':
        value += 1
    elif char == 'e':
        value += 2
    elif char == 'i':
        value += 3
    elif char == 'o':
        value += 4
    elif char == 'u':
        value += 5

print(value)

#алтернативно решение
#input_text = input()
#value = 0
#for i in range(0, len(input_text)):
#    if input_text[i] == 'a':
#        value += 1
#    if text[i] == 'e':
#        value += 2
#    if text[i] == 'i':
#        value += 3
#    if text[i] == 'o':
#        value += 4
#    if text[i] == 'u':
#        value += 5
#print(value)