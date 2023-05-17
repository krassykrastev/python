num_juniors = int(input())
num_seniors = int(input())
track_type = input()

money_collected = 0

if track_type == 'trail':
    money_collected = num_juniors * 5.50 + num_seniors * 7
elif track_type == 'cross-country':
    money_collected = num_juniors * 8 + num_seniors * 9.50
    if num_juniors + num_seniors >= 50:
        money_collected *= 0.75
elif track_type == 'downhill':
    money_collected = num_juniors * 12.25 + num_seniors * 13.75
elif track_type == 'road':
    money_collected = num_juniors * 20 + num_seniors * 21.50

money_collected *= 0.95

print(f'{money_collected:.2f}')
