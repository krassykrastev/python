# Our favorite super-spy action hero Sam is back from his vacation, and it is time to go on a mission.
# He needs to unlock a safe locked by several locks in a row, which all have varying sizes.
# The hero possesses a special weapon called the Key Revolver, with special bullets. Each bullet can unlock a lock with
# a size equal to or larger than the size of the bullet. The bullet goes into the keyhole, then explodes, completely
# destroying it. Sam doesn't know the size of the locks, so he needs to just shoot at all of them until the safe runs out of locks.
# What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn enemy – Nikoladze, keeps his
# top-secret Georgian Chacha Brandy recipe inside. It's valued differently across different times of the year, so Sam's
# boss will tell him what it's worth over the radio. One last thing, every bullet Sam fires will also cost him money,
# which will be deducted from his pay from the price of the intelligence.
# Good luck, operative.
# Input
# •	On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
# •	On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
# •	On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
# •	On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
# •	On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
# After Sam receives all of his information and gear (input), he starts to shoot the locks front-to-back while going
# through the bullets back-to-front.
# If he successfully destroyed a lock, print "Bang!", then remove the lock. If not, print "Ping!", leaving the lock
# intact. The bullet is removed in both cases.
# If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting.
# If there aren't any bullets left, don't print it.
# The program ends when Sam runs out of bullets or the safe runs out of locks.
# Output
# •	If Sam manages to open the safe, print:
# "{bullets_left} bullets left. Earned ${money_earned}"
# •	Otherwise, print:
# "Couldn't get through. Locks left: {locks_left}"
# Make sure to include the price of the bullets when calculating the money earned.
#
# Input1:
# 50
# 2
# 11 10 5 11 10 20
# 15 13 16
# 1500
#
# Output1:
# Ping!
# Bang!
# Reloading!
# Bang!
# Bang!
# Reloading!
# 2 bullets left. Earned $1300
#
# Input2:
# 20
# 6
# 14 13 12 11 10 5
# 13 3 11 10
# 800
#
# Output2:
# Bang!
# Ping!
# Ping!
# Ping!
# Ping!
# Ping!
# Couldn't get through. Locks left: 3
#
# Input3:
# 33
# 1
# 12 11 10
# 10 20 30
# 100
#
# Output3:
# Bang!
# Reloading!
# Bang!
# Reloading!
# Bang!
# 0 bullets left. Earned $1

from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value_of_intelligence = int(input())

total_price = 0
bullets_left = gun_barrel_size

while bullets and locks:

    current_bullet = bullets.pop()
    bullets_left -= 1

    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.insert(0, current_lock)

    total_price += price_per_bullet

    if bullets_left == 0 and bullets:
        print("Reloading!")
        bullets_left = gun_barrel_size

if not locks:
    value_of_intelligence -= total_price
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
