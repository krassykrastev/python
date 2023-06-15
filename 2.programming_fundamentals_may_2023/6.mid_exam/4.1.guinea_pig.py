# Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store
# and buys him everything he needs – food, hay, and cover.
# On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for a month (30 days).
# On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food.
# Every second day Merry first feeds the pet, then gives it a certain amount of hay equal to 5% of the rest of the food.
# On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!
# Input
# •	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
# Output
# •	If the food, the hay, and the cover are enough, print:
#   o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
# •	If one of the things is not enough, print:
#   o	"Merry must go to the pet store!"
# The output values must be formatted to the second decimal place!
#
# Input1:
# 10
# 5
# 5.2
# 1
#
# Output2: Everything is fine! Puppy is happy! Food: 1.00, Hay: 1.10, Cover: 1.87.
#
# Input2:
# 1
# 1.5
# 3
# 1.5
#
# Output2: Merry must go to the pet store!
#
# Input3:
# 9
# 5
# 5.2
# 1
#
# Output3: Merry must go to the pet store!

food = float(input())
hay = float(input())
cover = float(input())
guinea_weight = float(input())

cover_consumed = guinea_weight / 3
food_consumed = 0

for day in range(1, 31):
    food_consumed += 0.3
    food -= 0.3
    if day % 2 == 0:
        hay_consumed = food * 0.05
        hay -= hay_consumed
        food_consumed += hay_consumed

    if day % 3 == 0:
        cover -= cover_consumed

if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! "
          f"Food: {food:.2f}, "
          f"Hay: {hay:.2f}, "
          f"Cover: {cover:.2f}.")

else:
    print("Merry must go to the pet store!")