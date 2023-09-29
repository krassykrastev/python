# Write a concatenate() function that receives some strings as arguments and some named arguments (the key will be a string, and the value will be another string).
# First, you should concatenate all arguments successively. Next, take each key successively, and if it is present in the resulting string, change all matching parts with the key's value. In the end, return the final string.
#  See the examples for more clarification.
#
# Input1:
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
#
# Output1:
# SoftUniIsGreat!
#
# Input2:
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
#
# Output2:
# I Love Python

def concatenate(*args, **kwargs):
    result = ''
    for string in args:
        result += string
    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
