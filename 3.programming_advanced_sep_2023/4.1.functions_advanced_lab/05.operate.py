# Write a function called operate that receives an operator ("+", "-", "*" or "/") as а first argument and multiple
# numbers (integers) as additional arguments (*args). The function should return the result of the operator applied to
# all the numbers. For more clarification, see the examples below. Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division
#
# Input1:
# print(operate("+", 1, 2, 3))
#
# Output1:
# 6
#
# Input2:
# print(operate("*", 3, 4))
#
# Output2:
# 12

def operate(sign, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def divide():
        result = args[0]
        for index in range(1, len(args)):
            result /= args[index]
        return result

    if sign == "+":
        return add()
    elif sign == "-":
        return subtract()
    elif sign == "*":
        return multiply()
    elif sign == "/":
        return divide()

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
