# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# • If the data type is an int, multiply the number by 2.
# • If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# • If the data type is a string, surround the input with "$".
# Print the result on the console.
#
# Input1:
# int
# 5
#
# Output1: 10
#
# Input2:
# real
# 2
#
# Output2: 3.00
#
# Input3:
# string
# hello
#
# Output3: $hello$

def processing(line_one, line_two):
    result = 0
    if line_one == 'int':
        result = int(line_two) * 2
        return result
    elif line_one == 'real':
        result = float(line_two) * 1.5
        return f'{result:.2f}'
    elif line_one == 'string':
        result = f'${line_two}$'
        return result

first_line = input()
second_line = input()

print(processing(first_line, second_line))