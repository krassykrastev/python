steps = 0
steps_needed = 10000

while steps < steps_needed:
    command = input()
    if command == 'Going home':
        steps_to_home = int(input())
        steps += steps_to_home
        break
    steps += int(command)

diff = abs(steps - steps_needed)

if steps >= steps_needed:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
