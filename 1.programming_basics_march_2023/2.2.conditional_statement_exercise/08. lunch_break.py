from math import ceil
series_name = input()
series_time_needed = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

free_time = break_duration - lunch_time - relax_time
diff = ceil(abs(free_time - series_time_needed))

if series_time_needed <= free_time:
    print(f'You have enough time to watch {series_name} and left with {diff} minutes free time.')

else:
    print(f"You don't have enough time to watch {series_name}, you need {diff} more minutes.")
