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