# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.
#
# Input1: 30
# Output1:
# 30% [%%%.......]
# Still loading...
#
# Input2: 50
# Output2:
# 50% [%%%%%.....]
# Still loading...
#
# Input3: 100
# Output3:
# 100% Complete!
# [%%%%%%%%%%]

def loading_bar(some_number):
    if some_number == 100:
        return '100% Complete!\n [%%%%%%%%%%]'
    loaded_percents = some_number // 10
    return f"{some_number}% [{'%' * loaded_percents}{'.' * (10 - loaded_percents)}]\nStill loading..."


number = int(input())
print(loading_bar(number))