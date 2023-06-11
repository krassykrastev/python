# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
# On the last line, print the liters in the tank.
#
# Input1:
# 5
# 20
# 100
# 100 100
# 20
#
# Output1:
# Insufficient capacity!
# 240
#
# Input2:
# 7
# 10
# 20
# 30
# 10
# 5
# 10
# 20
#
# Output2: 105
#
# Input3:
# 1
# 1000
#
# Output3:
# Insufficient capacity!
# 0
#
# Input4:
# 4
# 250
# 10
# 20
# 40
#
# Output4:
# Insufficient capacity!
# Insufficient capacity!
# Insufficient capacity!
# 250

number_of_lines = int(input())
tank_capacity = 255
water_counter = 0
for current_line in range(number_of_lines):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0: # not enough capacity
        print('Insufficient capacity!')
        continue
    tank_capacity -= liters_of_water
    water_counter += liters_of_water
print(water_counter)