n_days = int(input())
players_count = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

total_water = n_days * players_count * water_per_day_per_person
total_food = n_days * players_count * food_per_day_per_person

for day in range(1, n_days + 1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        break
    if day % 2 == 0:
        group_energy += 0.05 * group_energy
        total_water -= 0.3 * total_water
    if day % 3 == 0:
        group_energy += 0.1 * group_energy
        total_food -= total_food / players_count
    if day == n_days:
        break

if group_energy <= 0:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")