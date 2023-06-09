# You are given a secret message you should decipher. To do that, you need to know that in each word:
# • the second and the last letter are switched (e.g., Holle means Hello)
# • the first letter is replaced by its character code (e.g., 72 means H)
#
# Input1: 72olle 103doo 100ya
# Output1: Hello good day
#
# Input2: 82yade 115te 103o
# Output2: Ready set go

secret_msg = input().split(' ')

for word in secret_msg:
    ascii_code = ''
    deciphered_word = ''
    for character in range(len(word)):
        current_character = word[character]
        if current_character.isdigit():
            ascii_code += str(current_character)
        else:
            deciphered_word += current_character
    first_character = chr(int(ascii_code))
    deciphered_word = first_character + deciphered_word
    deciphered_word = list(deciphered_word)
    deciphered_word[1], deciphered_word[-1] = deciphered_word[-1], deciphered_word[1]

    print(*deciphered_word, sep ='', end =' ')