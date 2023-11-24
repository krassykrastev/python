# Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the result of a function with the
# given tag, and return the new result. For more clarification, see the examples below
#
# Test Code1:
# @tags('p')
# def join_strings(*args):
#     return "".join(args)
# print(join_strings("Hello", " you!"))
#
# Output1:
# <p>Hello you!</p>
#
# Test Code2:
# @tags('h1')
# def to_upper(text):
#     return text.upper()
# print(to_upper('hello'))
#
# Output2:
# <h1>HELLO</h1>

def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

print()


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
