from collections import deque

tools = deque(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while challenges:
    first_current_tool = tools.popleft()

    current_multiply = first_current_tool * substances[-1]

    for index, number in enumerate(challenges):
        if number == current_multiply:
            challenges.pop(index)
            substances.pop()
            break

    else:
        tools.append(first_current_tool + 1)
        substances[-1] -= 1
        if not substances[-1] > 0:
            substances.pop()

    if not substances:
        break

print("Harry is lost in the temple. Oblivion awaits him.") if challenges \
    else print(f"Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")