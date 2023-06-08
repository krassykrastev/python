# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# • "OutOfStock {gift}"
#    o Find the gifts with this name in your collection, if any, and change their values to "None".
# • "Required {gift} {index}"
#    o If the index is valid, replace the gift on the given index with the given gift.
# • "JustInCase {gift}"
#    o Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
#
# Input1:
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money
#
# Output1: StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg
#
# Input2:
# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money
#
# Output2: Sweets Cozonac Chocolate Flowers Wine Eggs Hat

list_of_gifts = input().split(' ')

while True:
    commands = input().split(' ')
    if commands == ['No', 'Money']:
        break
    elif 'OutOfStock' in commands:
        for i in range(len(list_of_gifts)):
            if list_of_gifts[i] == commands[1]:
                list_of_gifts[i] = 'None'
    elif 'Required' in commands:
        if 0 <= int(commands[2]) < len(list_of_gifts):
            list_of_gifts[int(commands[2])] = commands[1]
    elif 'JustInCase' in commands:
        list_of_gifts[-1] = commands[1]

for gift in list_of_gifts:
    if gift != 'None':
        print(gift, end= ' ')