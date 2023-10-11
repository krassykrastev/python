# Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word.
# Use the pyfiglet module
# Input1:
# Hello World!
#
# Input2:
# Python 3.8

from pyfiglet import figlet_format

text = input()
ascii_art = figlet_format(text)

print(ascii_art)
