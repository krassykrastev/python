from collections import deque

programmers_time = deque(map(int, input().split()))
number_of_stacks = deque(map(int, input().split()))

rubber_duck = {
    "Darth Vader Ducky": [range(61), 0],
    "Thor Ducky": [range(61, 121), 0],
    "Big Blue Rubber Ducky": [range(121, 181), 0],
    "Small Yellow Rubber Ducky": [range(181, 241), 0]
}

while programmers_time and number_of_stacks:
    current_programmer_time = programmers_time.popleft()
    current_number_of_stack = number_of_stacks.pop()

    for name, value in rubber_duck.items():

        current_sum = current_programmer_time * current_number_of_stack
        if current_sum in value[0]:
            rubber_duck[name] = [value[0], value[1] + 1]
            break

    else:
        programmers_time.append(current_programmer_time)
        number_of_stacks.append(current_number_of_stack - 2)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded: ")

for name, value in rubber_duck.items():
    print(f"{name}: {value[1]}")