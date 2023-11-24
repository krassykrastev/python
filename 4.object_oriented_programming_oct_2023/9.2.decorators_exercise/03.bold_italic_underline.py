# Create three decorators: make_bold, make_italic, and make_underline, which will have to wrap a text returned from a
# function in <b></b>, <i></i> and <u></u> respectively.
#
# Test Code1:
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
# print(greet("Peter"))
#
# Output1:
# <b><i><u>Hello, Peter</u></i></b>
#
# Test Code2:
# @make_bold
# @make_italic
# @make_underline
# def greet_all(*args):
#     return f"Hello, {', '.join(args)}"
#
# print(greet_all("Peter", "George"))
#
# Output2:
# <b><i><u>Hello, Peter, George</u></i></b>

def make_bold(func):
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"
    return wrapper


def make_italic(func):
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"
    return wrapper


def make_underline(func):
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

print()

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
