def accommodate_new_pets(capacity, max_weight, *args):
    pets = {}
    not_enough_capacity = False
    for pet in args:
        if not capacity:
            not_enough_capacity = True
            break

        pet_type = pet[0]
        pet_weight = pet[1]
        if pet_weight > max_weight:
            continue
        capacity -= 1
        if pet_type not in pets:
            pets[pet_type] = 0

        pets[pet_type] += 1

    result = []

    if not_enough_capacity:
        result.append("You did not manage to accommodate all pets!")
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")

    [result.append(f"{pet}: {x}") for pet, x in sorted(pets.items())]
    return '\n'.join(result)


print(accommodate_new_pets(10, 15.0, ("cat", 5.8), ("dog", 10.0), ))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))