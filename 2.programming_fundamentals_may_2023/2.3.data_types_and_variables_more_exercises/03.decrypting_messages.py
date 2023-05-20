string = ''
decrypt_key = int(input())
number_of_lines = int(input())
for i in range(number_of_lines):
    current_character = input()
    string += chr(ord(current_character) + decrypt_key)
print(string)