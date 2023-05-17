musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

number_of_groups = int(input())
total_number_of_climbers = 0

for i in range(number_of_groups):
    group_size = int(input())
    total_number_of_climbers += group_size

    if group_size <= 5:
        musala_count += group_size
    elif group_size <= 12:
        montblanc_count += group_size
    elif group_size <= 25:
        kilimanjaro_count += group_size
    elif group_size <= 40:
        k2_count += group_size
    else:
        everest_count += group_size

musala_percent = musala_count / total_number_of_climbers * 100
montblanc_percent = montblanc_count / total_number_of_climbers * 100
kilimanjaro_percent = kilimanjaro_count / total_number_of_climbers * 100
k2_percent = k2_count / total_number_of_climbers * 100
everest_percent = everest_count / total_number_of_climbers * 100

print(f'{musala_percent:.2f}%')
print(f'{montblanc_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
