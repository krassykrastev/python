# String Manipulator - Group 2
# Create a program that executes changes over a string. First, you are going to receive the string, then commands.
# You will be receiving commands until the "Done" command. There are six possible commands:
# •	"Change {char} {replacement}"
# o	Replace all occurences of {char} with {replacement}, then print the string.
# •	"Includes {string}"
# o	Check if the string includes with {string} and print "True/False".
# •	"End {string}"
# o	Check if the string ends with {string} and print "True/False".
# •	"Uppercase"
# o	Make the whole string uppercased, then print it.
# •	"FindIndex {char}"
# o	Find the first index of {char}, then print it.
# •	"Cut {startIndex} {length}"
# o	Remove all characters from the string except for those starting from {startIndex} and the next {length} characters, then print it.
# Input
# •	On the 1st line you are going to receive the string.
# •	On the next lines, until the "Done" command is received, you will be receiving commands.
# •	All commands are case sensitive.
# •	The input will always be valid.
# Output
# •	Print the output of every command in the format described above.
#
# Input1:
# //Th1s 1s my str1ng!//
# Change 1 i
# Includes string
# End my
# Uppercase
# FindIndex I
# Cut 5 5
# Done
#
# Output1:
# //This is my string!//
# True
# False
# //THIS IS MY STRING!//
# 4
# S IS

initial_string = input()

line = input()
while not line == "End":
    data = line.split()
    command = data[0]
    if command == "Translate":
        char = data[1]
        replacement = data[2]
        initial_string = initial_string.replace(char, replacement)
        print(initial_string)
    elif command == "Includes":
        string = data[1]
        if string in initial_string:
            print("True")
        else:
            print("False")
    elif command == "Start":
        string = data[1]
        print(initial_string.startswith(string))
    elif command == "Lowercase":
        initial_string = initial_string.lower()
        print(initial_string)
    elif command == "FindIndex":
        char = data[1]
        print(initial_string.rindex(char))
    elif command == "Remove":
        start_i = int(data[1])
        count = int(data[2])
        to_remove = initial_string[start_i:start_i + count]
        initial_string = initial_string.replace(to_remove, "", 1)
        print(initial_string)
    line = input()