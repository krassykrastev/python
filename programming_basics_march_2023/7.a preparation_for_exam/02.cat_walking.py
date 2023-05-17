walk_minutes = int(input())
num_walks = int(input())
calories_per_day = int(input())

total_calories_burned = num_walks * walk_minutes * 5
percent_calories_burned = total_calories_burned / calories_per_day * 100

if percent_calories_burned >= 50:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.')
