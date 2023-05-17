season = input()
group_type = input()
num_students = int(input())
num_nights = int (input())

price = 0
sport =''

if season == 'Winter':
    if group_type == 'boys':
        price = num_students * num_nights * 9.60
        sport = 'Judo'
    elif group_type == 'girls':
        price = num_students * num_nights * 9.60
        sport = 'Gymnastics'
    elif group_type == 'mixed':
        price = num_students * num_nights * 10
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'boys':
        price = num_students * num_nights * 7.20
        sport = 'Tennis'
    elif group_type == 'girls':
        price = num_students * num_nights * 7.20
        sport = 'Athletics'
    elif group_type == 'mixed':
        price = num_students * num_nights * 9.5
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys':
        price = num_students * num_nights * 15
        sport = 'Football'
    elif group_type == 'girls':
        price = num_students * num_nights * 15
        sport = 'Volleyball'
    elif group_type == 'mixed':
        price = num_students * num_nights * 20
        sport = 'Swimming'

if num_students >= 50:
    price *= 0.50
elif 20 <= num_students < 50:
    price *= 0.85
elif 10 <= num_students < 20:
    price *= 0.95

print(f'{sport} {price:.2f} lv.')
