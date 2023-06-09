from math import floor

number_of_biscuits_per_worker = int(input())
count_of_workers = int(input())
number_biscuits_per_30_days = int(input())

total_biscuits_made = 0
for day in range(1, 31):
    workers_capacity = count_of_workers * number_of_biscuits_per_worker
    if day % 3 == 0:
        workers_capacity *= 0.75
    total_biscuits_made += workers_capacity
    total_biscuits_made = floor(total_biscuits_made)

print(f"You have produced {total_biscuits_made} biscuits for the past month.")

diff = abs(total_biscuits_made - number_biscuits_per_30_days)
percent = (diff / number_biscuits_per_30_days) * 100

if total_biscuits_made > number_biscuits_per_30_days:
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    print(f"You produce {percent:.2f} percent less biscuits.")