length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input()) / 100 #input is in number it has to be converted to percent

volume_cm = length_cm * width_cm * height_cm
# 1l = 1 dcm3 or 10 * 10 * 10 cm or 1000 cm

volume_liters = volume_cm / 1000

water_percent = 1 - percent
water_needed = volume_liters * water_percent

print(water_needed)
