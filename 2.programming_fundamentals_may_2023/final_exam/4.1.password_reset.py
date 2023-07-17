# Yet again, you have forgotten your password. Naturally, it's not the first time this has happened.
# Actually, you got so tired of it that you decided to help yourself with an intelligent solution.
# Write a password reset program that performs a series of commands upon a predefined string.
# First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with
# commands split by a single space. The commands will be the following:
# •	"TakeOdd"
#   o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
# •	"Cut {index} {length}"
#   o	Gets the substring with the given length starting from the given index from the password and removes its first
#   occurrence, then prints the password on the console.
#   o	The given index and the length will always be valid.
# •	"Substitute {substring} {substitute}"
#   o	If the raw password contains the given substring, replaces all of its occurrences with the substitute text given
#   and prints the result.
#   o	If it doesn't, prints "Nothing to replace!".
#
# Input1:
# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done
#
# Output1:
# icecream::hot::summer
# icecream::hot::mer
# icecream-hot-mer
# Nothing to replace!
# Your password is: icecream-hot-mer
#
# Input2:
# up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy
# TakeOdd
# Cut 18 2
# Substitute ! ***
# Substitute ? .!.
# Done
#
# Output2:
# programming!is!funny
# programming!is!fun
# programming***is***fun
# Nothing to replace!
# Your password is: programming***is***fun

data = input()

while True:
    command = input().split(" ")

    if command[0] == "Done":
        print(f"Your password is: {data}")
        break

    elif command[0] == "TakeOdd":
        take_odd_data = ""
        for i in range(len(data)):
            if i % 2 != 0:
                take_odd_data += data[i]
        data = take_odd_data
        # data = "".join([data[i] for i in range(len(data)) if i % 2 != 0])
        print(data)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        data = data[:index] + data[index+length:]
        # data = "".join([data[i] for i in range(len(data)) if i < index or i >= index + length])
        print(data)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]

        if substring in data:
            data = data.replace(substring, substitute)
            print(data)

        else:
            print("Nothing to replace!")
