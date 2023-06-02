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