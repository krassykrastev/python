current_hour = int(input())
current_minutes = int(input())

total_time_in_minutes = (current_hour * 60) + current_minutes
total_time_in_minutes += 15  # колко ще е часът след 15 минути

hours = total_time_in_minutes // 60 #делим целочислено да намерим колко са часовете само
minutes = total_time_in_minutes % 60 #делим модулно да намерим само остатъка, т.е. колко са минутите

if hours > 23:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')

else:
    print(f'{hours}:{minutes}')
