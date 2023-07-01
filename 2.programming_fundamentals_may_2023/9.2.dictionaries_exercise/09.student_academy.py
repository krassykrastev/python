# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
#
# Input1:
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5
#
# Output1:
# John -> 5.00
# Alice -> 4.50
# George -> 5.
#
# Input2:
# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6
#
# Output2:
# Rob -> 5.50
# Christian -> 5.00
# Robert -> 6.00

students = {}
pair_of_rows = int(input())

for i in range(pair_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name in students:
        students[student_name] = (students[student_name] + student_grade) / 2
    else:
        students[student_name] = student_grade

for student, grade in students.items():
    if grade >= 4.50:
        print(f"{student} -> {grade:.2f}")