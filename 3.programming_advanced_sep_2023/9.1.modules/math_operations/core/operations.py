def sum_nums(num, num2):
    return num + num2


def subtract(num, num2):
    return num - num2


def multiply(num, num2):
    return num * num2


def divide(num, num2):
    try:
        num / num2
    except ZeroDivisionError:
        return None


def power(num, num2):
    return num ** num2
