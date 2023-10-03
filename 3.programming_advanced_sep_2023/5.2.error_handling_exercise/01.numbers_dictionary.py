# You are provided with a code:
# •	On the first several lines, until you receive the command "Search", you will receive on separate lines the number as a text and the number as an integer
# •	When you receive "Search" on the next several lines until you receive the command "Remove", you will be given the searched number as a text, and you need to print it on the console
# •	When you receive "Remove" on the next several lines until you receive "End", you will be given the searched number as a text, and you need to remove it from the dictionary
# •	In the end, you need to print what is left from the dictionary
# There is some missing code in the solution, and some errors may occur. Complete the code, so the following errors are handled:
# •	Passing non-integer type to the variable number
# •	Searching for a non-existent number
# •	Removing a non-existent number
# Print appropriate messages when an error has occurred. The messages should be:
# •	"The variable number must be an integer"
# •	"Number does not exist in dictionary" - for non-existing keys
#
# Input1:
# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End
#
# Output1:
# 1
# {'one': 1}
#
# Input2:
# one
# two
# Search
# Remove
# End
#
# Output2:
# The variable number must be an integer
# {}
#
# Input3:
# one
# 1
# Search
# one
# Remove
# two
# End
#
# Output3:
# 1
# Number does not exist in dictionary
# {'one': 1}

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number
    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
