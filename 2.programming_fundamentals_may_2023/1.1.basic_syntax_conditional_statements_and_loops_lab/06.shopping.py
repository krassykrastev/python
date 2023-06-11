# Write a program that reads an integer number representing a budget.
# On the following lines, it reads integer numbers representing the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!" and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."
#
# Input1:
# 100
# 5
# End
#
# Output1: You bought everything needed.
#
# Input2:
# 50
# 25
# 20
# 10
#
# Output2: You went in overdraft!

budget = int(input())
total_price = 0

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break

    price = int(command)

    if total_price + price > budget:
        print('You went in overdraft!')
        break

    total_price += price
