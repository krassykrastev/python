from collections import deque

males = [int(i) for i in input().split()]
females = deque([int(i) for i in input().split()])

matches = 0

while males and females:

    current_male = males.pop()
    current_female = females.popleft()

    if current_female <= 0:
        males.append(current_male)
        continue

    if current_male <= 0:
        females.appendleft(current_female)
        continue

    if current_male % 25 == 0:
        next_male = males.pop()
        females.appendleft(current_female)
        continue

    elif current_female % 25 == 0:
        next_female = females.popleft()
        males.append(current_male)
        continue

    if current_male == current_female:
        matches += 1
        continue
    else:
        current_male -= 2
        males.append(current_male)
        continue


print(f"Matches: {matches}")


if not males:
    print(f"Males left: none")
else:
    males = males[::-1]
    print(f"Males left: {', '.join(map(str, males))}")

if not females:
    print(f"Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")