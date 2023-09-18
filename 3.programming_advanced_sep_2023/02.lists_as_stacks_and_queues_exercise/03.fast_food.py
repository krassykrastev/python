# You have a fast-food restaurant, and the food you are offering is previously prepared.
# Write a program that checks if you have enough food to serve lunch to all your customers. You also want to know who
# the client with the biggest order for that day is.
# First, you will be given the quantity of food you have for the day (an integer number). Next, you will be given a
# sequence of integers (separated by a single space), each representing the quantity of food in each order. Keep the
# orders in a queue. Find the biggest order and print it. Next, you will begin servicing your clients from the first one
# that came. Before each order, check if you have enough food left to complete it:
# •	If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
# •	Otherwise, stop serving.
# Input
# •	On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
# •	On the second line, you will receive a sequence of integers, representing each order, separated by a single space
# Output
# •	On the first line, print the quantity of the biggest order
# •	On the second line:
#   o	If you succeeded in servicing all your clients, print: "Orders complete".
#   o	Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
#
# Input1:
# 348
# 20 54 30 16 7 9
#
# Output1:
# 54
# Orders complete
#
# Input2:
# 499
# 57 45 62 70 33 90 88 76 100 50
#
# Output2:
# 100
# Orders left: 76 100 50

from collections import deque

quantity_of_food = int(input())
queue_of_orders = deque(map(int, input().split()))

print(max(queue_of_orders))

for i in range(len(queue_of_orders)):
    current_order = queue_of_orders[0]

    if quantity_of_food >= current_order:
        queue_of_orders.popleft()
        quantity_of_food -= current_order

if queue_of_orders:
    print("Orders left: ", end="")
    for i in range(len(queue_of_orders)):
        print(queue_of_orders[i], end=" ")

else:
    print("Orders complete")
