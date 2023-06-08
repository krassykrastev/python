# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros,
# and moves them to the back without messing up the other elements. Print the resulting integer list.
#
# Input1: 1, 0, 1, 2, 0, 1, 3
# Output1: [1, 1, 2, 1, 3, 0, 0]
#
# Input2: 0, 5, 0, 4, 0, 0, 5
# Output2: [5, 4, 5, 0, 0, 0, 0]

input_string = input().split(', ')

for i in range(len(input_string)):
    if input_string[i] == '0':
        input_string.remove('0')
        input_string.append('0')

for j in range(len(input_string)):
    input_string[j] = int(input_string[j])

# input_string = list(map(int, input_string)) # #another way of converting the strings in the list to integers

print(input_string)