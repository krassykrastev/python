number_days_off = int(input())

time_to_play_during_work_days = (365 - number_days_off) * 63
time_to_play_during_days_off = number_days_off * 127
total_time_to_play = time_to_play_during_work_days + time_to_play_during_days_off

diff_mins = abs(30000 - total_time_to_play)

diff_hrs = diff_mins // 60 # дава цялото число от делението, или часовете
diff_minutes = diff_mins % 60 #дава остатъка от делението, или минутите

if total_time_to_play <= 30000:
    print('Tom sleeps well')
    print(f'{diff_hrs} hours and {diff_minutes} minutes less for play')

else:
    print('Tom will run away')
    print(f'{diff_hrs} hours and {diff_minutes} minutes more for play')


