string = ''
c = o = n = 0
current_word = ''

while True:
    command = input()
    if command == 'End':
        break
    if ord(command) < 65 or (90 < ord(command) < 97) or ord(command) > 122:
        continue
    if command == 'c' and c != 1 or command == 'o' and o != 1 or command == 'n' and n != 1:
        if command == 'c': c = 1
        if command == 'o': o = 1
        if command == 'n': n = 1
    else:
        string += command

    if c == 1 and o == 1 and n == 1:
        current_word += string + " "
        string = ''
        c = o = n = 0

print(current_word)
