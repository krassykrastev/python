# You are an astronaut who just embarked on a mission across the solar system.
# Since you will be in space for a long time, you have packed a lot of food with you.
# Create a program, which helps you identify how much food you have left and gives you information about its expiration date.
# On the first line of the input, you will be given a text string.
# You must extract the information about the food and calculate the total calories.
# First, you must extract the food info. It will always follow the same pattern rules:
# •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
# #{item name}#{expiration date}#{calories}#   or
# |{item name}|{expiration date}|{calories}|
# •	The item name will contain only lowercase and uppercase letters and whitespace
# •	The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long
# •	The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have.
# Keep in mind that you need 2000kcal a day.
# Input / Constraints
# •	You will receive a single string
# Output
# •	First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
# •	The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"
#
# Input1: #Bread#19/03.core/21#4000#|Invalid|03.core/03.core.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|
#
# Output1:
# You have food to last you for: 2 days!
# Item: Bread, Best before: 19/03.core/21, Nutrition: 4000
# Item: Apples, Best before: 08/10/20, Nutrition: 200
# Item: Carrots, Best before: 06/08/20, Nutrition: 500
#
# Input2: $$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.core.20#450|$5*(@!#Ice Cream#03.core/10/21#9000#^#@aswe|Milk|05.core/09/20|2000|
#
# Output2:
# You have food to last you for: 9 days!
# Item: Fish, Best before: 24/12/20, Nutrition: 8500
# Item: Ice Cream, Best before: 03.core/10/21, Nutrition: 9000
# Item: Milk, Best before: 05.core/09/20, Nutrition: 2000
#
# Input3: Hello|#Invalid food#19/03.core/20#450|$5*(@
#
# Output3: You have food to last you for: 0 days!

import re

total_calories = 0

text = input()

pattern = r"([#|])(?P<item>[a-zA-Z ]+)\1(?P<exp_date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,5})\1"

matches = re.finditer(pattern, text)
food_data = []

for match in matches:
    object_dict = match.groupdict()
    food_data.append(object_dict)
    total_calories += int(object_dict['calories'])

days_to_last = total_calories // 2000

print(f"You have food to last you for: {days_to_last} days!")

for food in food_data:
    print(f"Item: {food['item']}, Best before: {food['exp_date']}, Nutrition: {food['calories']}")
