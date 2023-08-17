from _collections import deque

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
