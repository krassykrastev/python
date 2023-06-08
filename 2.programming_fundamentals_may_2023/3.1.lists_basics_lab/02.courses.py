# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.
#
# Input1:
# 2
# PB Python
# PF Python
#
# Output1: ['PB Python', 'PF Python']
#
# Input2:
# 4
# Front-End
# C# Web
# JS Core
# Programming Fundamentals
#
# Output2: ['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']

n = int(input())
courses_data = []

for i in range(n):
    course_name = input()
    courses_data.append(course_name)

print(courses_data)