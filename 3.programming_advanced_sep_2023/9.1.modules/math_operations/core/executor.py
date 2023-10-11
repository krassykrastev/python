from math_operations.core.operations import sum_nums, subtract, multiply, divide, power

sign_mapper = {
    "+": sum_nums,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power
}


def execute_string(string):
    num1, sign, num2 = string.split()
    num1 = float(num1)
    num2 = float(num2)
    return sign_mapper[sign](num1, num2)
