annual_fee = int(input())

sneakers = annual_fee - (annual_fee * 0.40)
equip = sneakers - (sneakers * 0.2)
ball = equip * 0.25
accessories = ball * 0.20

expenses = annual_fee + sneakers + equip + ball + accessories
print(expenses)
