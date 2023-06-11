# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky.
# Create a program that receives a person's age and prints what he/she drinks.
# Rules:
# A kid is defined as someone under or at the age of 14.
# A teen is defined as someone under or at the age of 18.
# A young adult is defined as someone under or at the age of 21.
# An adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!
#
# Input1: 13
# Output1: drink toddy
#
# Input2: 17
# Output2: drink coke
#
# Input3: 21
# Output3: drink beer
#
# Input4: 30
# Output4: drink whisky

ages = int(input())
drink = ''

if ages <= 14:
    drink = 'toddy'
elif ages <= 18:
    drink = 'coke'
elif ages <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'drink {drink}')
