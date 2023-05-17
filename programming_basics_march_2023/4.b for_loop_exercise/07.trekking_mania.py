group_count = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
total_people = 0

for i in range(group_count):
    people_count = int(input())
    total_people += people_count
    if people_count <= 5:
        p1 += people_count
    elif people_count <= 12:
        p2 += people_count
    elif people_count <= 25:
        p3 += people_count
    elif people_count <= 40:
        p4 += people_count
    elif people_count >= 41:
        p5 += people_count

p1_percent = p1 / total_people * 100
p2_percent = p2 / total_people * 100
p3_percent = p3 / total_people * 100
p4_percent = p4 / total_people * 100
p5_percent = p5 / total_people * 100

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')
