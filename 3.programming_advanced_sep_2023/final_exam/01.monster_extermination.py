from collections import deque

monster = deque(map(int, input().split(",")))
streng_of_a_strike = list(map(int, input().split(",")))
killed_monsters = 0

while streng_of_a_strike and monster:
    current_armor = monster.popleft()
    current_strike = streng_of_a_strike.pop()

    if current_strike >= current_armor:
        killed_monsters += 1
        current_strike -= current_armor
        if streng_of_a_strike:
            streng_of_a_strike[-1] += current_strike

        else:
            if current_strike:
                streng_of_a_strike.append(current_strike)

    else:
        current_armor -= current_strike
        monster.append(current_armor)

if not monster:
    print("All monsters have been killed!")
if not streng_of_a_strike:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")