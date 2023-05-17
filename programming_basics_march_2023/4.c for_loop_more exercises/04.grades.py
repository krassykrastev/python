num_students = int(input())

total_score = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0

for i in range(num_students):
    current_student_score = float(input())
    total_score += current_student_score
    if current_student_score <= 2.99:
        p1 += 1
    elif current_student_score <= 3.99:
        p2 += 1
    elif current_student_score <= 4.99:
        p3 += 1
    elif current_student_score >= 5.00:
        p4 += 1

average_score = total_score / num_students
p1_percentage = p1 / num_students * 100
p2_percentage = p2 / num_students * 100
p3_percentage = p3 / num_students * 100
p4_percentage = p4 / num_students * 100

print(f'Top students: {p4_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {p3_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {p2_percentage:.2f}%')
print(f'Fail: {p1_percentage:.2f}%')
print(f'Average: {average_score:.2f}')
