# You will be given strings on separate lines until you receive an "end" command.
# Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".
#
# Input1:
# helLo
# Softuni
# bottle
# end
#
# Output1:
# helLo = oLleh
# Softuni = inutfoS
# bottle = elttob
#
# Input2:
# Dog
# caT
# chAir
# end
#
# Output2:
# Dog = goD
# caT = Tac
# chAir = riAhc

while True:
    command = input()

    if command == "end":
        break

    print(f"{command} = {command[::-1]}")