time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time_in_sec = time_first + time_second + time_third
minutes = total_time_in_sec // 60 #делим без остатък, за да видим само колко е цялото число, т.е. минутите
seconds = total_time_in_sec % 60 #делим модулно, за да получим само остатъка

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
