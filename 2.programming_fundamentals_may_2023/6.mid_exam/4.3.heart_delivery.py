# Valentine's day is coming, and Cupid has minimal time to spread some love across the neighborhood. Help him with his mission!
# You will receive a string with even integers, separated by a "@" - this is our neighborhood.
# After that, a series of Jump commands will follow until you receive "Love!".
# Every house in the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate Valentine's day.
# The integers in the neighborhood indicate those needed hearts.
# Cupid starts at the position of the first house (index 0) and must jump by a given length. The jump commands will be in this format: "Jump {length}".
# Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2:
# •	If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has Valentine's day."
# •	If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
# •	Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and if he does jump outside of it,
# he should start from the first house again (index 0)
# For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2.
# He will end up at index 2 and decrease the needed hearts by 2: [6, 6, 4].
# Next, he jumps again with a length of 2 and goes outside the neighborhood, so he goes back to the first house (index 0) and
# again decreases the needed hearts there: [4, 6, 4].
# Input
# •	On the first line, you will receive a string with even integers separated by "@" – the neighborhood and the number of hearts for each house.
# •	On the next lines, until "Love!" is received, you will be getting jump commands in this format: "Jump {length}".
# Output
# In the end, print Cupid's last position and whether his mission was successful or not:
# •	"Cupid's last position was {last_position_index}."
# •	If each house has had Valentine's day, print:
# o	"Mission was successful."
# •	If not, print the count of all houses that didn't celebrate Valentine's Day:
# o	"Cupid has failed {houseCount} places."
# Constraints
# •	The neighborhood's size will be in the range [1…20]
# •	Each house will need an even number of hearts in the range [2 … 10]
# •	Each jump length will be an integer in the range [1 … 20]
#
# Input1:
# 10@10@10@2
# Jump 1
# Jump 2
# Love!
#
# Output1:
# Place 3 has Valentine's day.
# Cupid's last position was 3.
# Cupid has failed 3 places.
#
# Input2:
# 2@4@2
# Jump 2
# Jump 2
# Jump 8
# Jump 3
# Jump 1
# Love!
#
# Output2:
# Place 2 has Valentine's day.
# Place 0 has Valentine's day.
# Place 0 already had Valentine's day.
# Place 0 already had Valentine's day.
# Cupid's last position was 1.
# Cupid has failed 1 places.

failed_houses = 0
length = 0

neighborhood = [int(house) for house in input().split("@")]
jump_info = input()
neighborhood_len = len(neighborhood)

while jump_info != "Love!":
    length += int(jump_info.split()[-1])
    if length >= neighborhood_len:
        length = 0

    if neighborhood[length] > 2:
        neighborhood[length] -= 2
    else:
        if neighborhood[length] != 0:
            neighborhood[length] -= 2
            print(f"Place {length} has Valentine's day.")
        else:
            print(f"Place {length} already had Valentine's day.")
        # print(f"Place {length} {text} Valentine's day.")
    jump_info = input()

print(f"Cupid's last position was {length}.")

for house in neighborhood:
    if house != 0:
        failed_houses += 1

if failed_houses > 0:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")

# neighborhood = [int(x) for x in input().split("@")]
# jump_data = input()
# neighborhood_len = len(neighborhood)
# length = 0
#
# while jump_data != "Love!":
#     length += int(jump_data.split()[-1])
#     if length >= neighborhood_len:
#         length = 0
#
#     if neighborhood[length] > 2:
#         neighborhood[length] -= 2
#     else:
#         if neighborhood[length] != 0:
#             neighborhood[length] -= 2
#             text = "has"
#         else:
#             text = "already had"
#         print(f"Place {length} {text} Valentine's day.")
#     jump_data = input()
#
# print(f"Cupid's last position was {length}.")
#
# failed_houses = sum(1 for x in neighborhood if x != 0)
#
# if failed_houses:
#     print(f"Cupid has failed {failed_houses} places.")
# else:
#     print("Mission was successful.")