# There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP.
# When a guest comes, check if they exist on any of the two reservation lists. On the first line, you will receive the
# number of guests – N. On the following N lines, you will be receiving their reservation codes. All reservation codes
# are 8 characters long, and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be
# unique. After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of guests who did not come to the party and their reservation numbers:
# •	The VIP guests must be first.
# •	Both the VIP and the Regular guests must be sorted in ascending order.
#
# Input1:
# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END
#
# Output1:
# 2
# 7IK9Yo0h
# tSzE5t0p
#
# Input2:
# 6
# m8rfQBvl
# fc1oZCE0
# UgffRkOn
# 7ugX7bm0
# 9CQBGUeJ
# 2FQZT3uC
# 2FQZT3uC
# 9CQBGUeJ
# fc1oZCE0
# END
#
# Output2:
# 3
# 7ugX7bm0
# UgffRkOn
# m8rfQBvl

n = int(input())
reservations = set()

for i in range(n):
    rev_number = input()
    reservations.add(rev_number)

guest = input()
while guest != "END":
    reservations.remove(guest)
    guest = input()

print(len(reservations))

for num in sorted(reservations):
    print(num)
