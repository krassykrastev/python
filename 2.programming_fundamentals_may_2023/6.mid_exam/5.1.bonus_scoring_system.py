# Create a program that calculates bonus points for each student enrolled in a course.
# On the first line, you are going to receive the number of the students.
# On the second line, you will receive the total number of lectures in the course.
# The course has an additional bonus, which you will receive on the third line.
# On the following lines, you will be receiving the count of attendances for each student.
# The bonus is calculated with the following formula:
# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
# Find the student with the maximum bonus and print them, along with his attendances, in the following format:
# "Max Bonus: {max bonus points}."
# "The student has attended {student attendances} lectures."
# Round the bonus points at the end to the nearest larger number.
# Input / Constrains
# •	On the first line, you are going to receive the number of the students – an integer in the range [0…50]
# •	On the second line, you will receive the number of the lectures – an integer number in the range [0...50].
# •	On the third line, you will receive the additional bonus – an integer number in the range [0….100].
# •	On the following lines, you will be receiving the attendance of each student.
# •	There will never be students with equal bonuses.
# Output
# •	Print the maximum bonus points and the attendances of the given student, rounded to the nearest larger number,
# scored by a student in this course in the format described above.
#
# Input1:
# 5
# 25
# 30
# 12
# 19
# 24
# 16
# 20
#
# Output1:
# Max Bonus: 34.
# The student has attended 24 lectures.
#
# Input2:
# 10
# 30
# 14
# 8
# 23
# 27
# 28
# 15
# 17
# 25
# 26
# 5
# 18
#
# Output2:
# Max Bonus: 18.
# The student has attended 28 lectures.

max_number = 0
total_bonus = 0

number_of_students = int(input())
course_lectures = int(input())
additional_bonus = int(input())

for student in range(number_of_students):
    number_of_lectures = int(input())
    if number_of_lectures > max_number:
        max_number = number_of_lectures

if max_number > 0:
    total_bonus = (max_number / course_lectures) * (5 + additional_bonus)

print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {max_number} lectures.")