# Write a program that:
# • Reads an input string
# • Reverses it using a stack
# • Prints the result back on the console
#
# Input1: I Love Python
# Output1: nohtyP evoL I
#
# Input2: Stacks and Queues
# Output2: seueuQ dna skcatS

string = list(input())

while len(string) > 0:
    current_character = string.pop()
    print(current_character, end="")
