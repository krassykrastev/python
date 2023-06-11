# As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
# His equipment consists of a helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.
# Input / Constraints
# The input will consist of 5 lines:
# • On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# • On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# • On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# • On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# • On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].
# Output
# • As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
#
# Input1:
# 7
# 2
# 3
# 4
# 5
#
# Output1: Gladiator expenses: 16.00 aureus
#
# Input2:
# 23
# 12.50
# 21.50
# 40
# 200
#
# Output2: Gladiator expenses: 608.00 aureus

number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // (2 * 3)
total_armor_broken = total_shield_broken // 2
expenses = total_helmet_broken * helmet_price \
           + total_sword_broken * sword_price \
           + total_shield_broken * shield_price \
           + total_armor_broken * armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')