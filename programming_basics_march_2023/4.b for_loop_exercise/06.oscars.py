actor_name = input()
points = float(input())
n = int(input())

nomination_points = 1250.5

for i in range(n):
    jury_name = input()
    jury_points = float(input())
    points += len(jury_name) * jury_points / 2

    if points > nomination_points:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
        break

if points <= nomination_points:
    print(f'Sorry, {actor_name} you need {nomination_points - points:.1f} more!')
