# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each character with
# the corresponding character three positions forward in the ASCII table. For example, A would be replaced with D, B
# would become E, and so on. Print the encrypted text.
#
# Input1: Programming is cool!
# Output1: Surjudpplqj#lv#frro$
#
# Input2: One year has 365 days.
# Output2: Rqh#|hdu#kdv#698#gd|v1

encrypted_message = ""

initial_message = input()

for character in initial_message:
    encrypted_message += chr(ord(character) + 3)

print(encrypted_message)