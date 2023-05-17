tournaments_count = int(input())
points = int(input())

tournaments_points = 0
wins = 0

for tournament in range(tournaments_count):
    tournament_score = input()
    if tournament_score == 'W':
        tournaments_points += 2000
        wins += 1
    elif tournament_score == 'F':
        tournaments_points += 1200
    elif tournament_score == 'SF':
        tournaments_points += 720

points += tournaments_points

print(f'Final points: {points}')
print(f'Average points: {tournaments_points // tournaments_count}') #закръгляме до най-близкото число надолу
print(f'{wins / tournaments_count * 100:.2f}%')
