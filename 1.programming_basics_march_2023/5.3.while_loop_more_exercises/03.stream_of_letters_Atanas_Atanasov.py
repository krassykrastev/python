output_string = ''
current_word = ''

c = False
n = False
o = False

command = input()
while command != 'End':
    if not c and command == 'c':
        c = True
    elif not o and command == 'o':
        o = True
    elif not n and command == 'n':
        n = True
    elif 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        current_word += command

    if c and o and n:
        output_string += current_word + ' '
        current_word = ''
        c = False
        o = False
        n = False

    command = input()

print(output_string)
