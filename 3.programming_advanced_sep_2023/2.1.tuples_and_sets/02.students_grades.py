# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a
# student's name and grade. For each student print all his/her grades and finally his/her average grade, formatted to
# the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.
#
# Input1:
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
#
# Output1:
# Mark -> 5.50 2.50 3.46 (avg: 3.82)
# Peter -> 5.20 3.20 (avg: 4.20)
# Alex -> 2.00 3.00 (avg: 2.50)
#
# Input2:
# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66
#
# Output2:
# Ted -> 3.00 3.66 (avg: 3.33)
# Scott -> 4.50 5.00 (avg: 4.75)
#
# Input3:
# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30
#
# Output3:
# Peter -> 4.40 (avg: 4.40)
# Lee -> 6.00 5.50 6.00 (avg: 5.83)
# Kenny -> 3.30 (avg: 3.30)

number_of_students = int(input())
students = {}

for i in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student_name, grades in students.items():
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f"{student_name} -> {formatted_grades} (avg: {sum(grades)/len(grades):.2f})")
