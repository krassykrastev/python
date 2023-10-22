from collections import deque

elements = {"Patch": [30, 0], "Bandage": [40, 0], "MedKit": [100, 0]}

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

while textiles and medicaments:
    first_value_of_textile = textiles.popleft()
    last_value_of_medicaments = medicaments.pop()
    their_sum = first_value_of_textile + last_value_of_medicaments

    for item, resources in elements.items():
        if their_sum == resources[0]:
            elements[item][1] += 1
            break

    else:
        if their_sum > elements["MedKit"][0]:
            elements["MedKit"][1] += 1
            their_sum -= elements["MedKit"][0]
            medicaments[-1] += their_sum

        else:
            last_value_of_medicaments += 10
            medicaments.append(last_value_of_medicaments)

sorted_elements = dict(sorted(elements.items(), key=lambda x: (-x[1][1], x[0])))
are_both_empty = False

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
    are_both_empty = True

else:
    print("Textiles are empty.") if not textiles else print("Medicaments are empty.")

[print(f"{item} - {resources[1]}") for item, resources in sorted_elements.items() if resources[1]]

if not are_both_empty:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}") if textiles \
        else print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")