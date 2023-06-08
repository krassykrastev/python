# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following: "multiply", "divide", "add", "subtract".
#
# Input1:
# subtract
# 5
# 4
#
# Output1: 1
#
# Input2:
# divide
# 8
# 4
#
# Output2: 2

def calculate_result(some_operator, number_1, number_2):
    if some_operator == 'multiply':
        return number_1 * number_2
    elif some_operator == 'divide':
        return int(number_1 / number_2)
    elif some_operator == 'add':
        return number_1 + number_2
    elif some_operator == 'subtract':
        return number_1 - number_2

operator = input()
num1 = int(input())
num2 = int(input())
print(calculate_result(operator, num1, num2))

# another more advanced solution with dictionaries
# def calculate_result(operator, num1, num2):
#     return{
#         'multiply': num1 * num2,
#         'divide': int(num1 / num2),
#         'add': num1 + num2,
#         'subtract': num1 - num2
#     }.get(operator, 'Invalid operator')
#
# operator = input()
# num1 = int(input())
# num2 = int(input())
# print(calculate_result(operator, num1, num2))