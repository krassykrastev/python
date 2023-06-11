# Jenny studies programming with Python and wants to create a program that greets the user when he/she gives his/her name.
# The greeting should be in the format "Hello, {name}!".
# However, Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!". Could you help her?
#
# Input1: Peter
# Output1: Hello, Peter!
#
# Input2: Amy
# Output2: Hello, Amy!
#
# Input3: Johnny
# Output3: Hello, my love!

name = input()

if name == 'Johnny':
    print('Hello, my love!')
else:
    print(f'Hello, {name}!')
