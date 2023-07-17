# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages.
# Go ahead and type it in!
# On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is
# given, you will receive strings with instructions for different operations that need to be performed upon the
# concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
#   o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
#   o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
#   o	If not, print "error".
#   o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
#   o	Changes all occurrences of the given substring with the replacement text.
#
# Input1:
# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal
#
# Output1:
# hellodar!gnil
# hellodarling!
# hello darling!
# You have a new text message: hello darling!
#
# Input2:
# Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal
#
# Output2:
# Howare?uoy
# Howareyou?
# error
# How areyou?
# How are you?
# You have a new text message: How are you?

data = input()

while True:

    command = input().split(':|:')

    if command[0] == "Reveal":
        break

    elif command[0] == "InsertSpace":
        index = int(command[1])
        data = data[:index] + " " + data[index:]
        print(data)

    elif command[0] == "Reverse":
        substring = command[1]

        if substring in data:
            data = data.replace(substring, "", 1)
            data = data + substring[::-1]
            print(data)

        else:
            print("error")

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        data = data.replace(substring, replacement)

        print(data)

print(f"You have a new text message: {data}")