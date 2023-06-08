# Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the course and
# all the exercises for the lessons. Before the course starts, there are some changes to be made.
# On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the next course,
# separated by a comma and a space ", ". Until you receive the "course start" command, you will be given some commands to modify the course schedule.
# The possible commands are:
# • "Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# • "Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# • "Remove:{lessonTitle}" - remove the lesson, if it exists.
# • "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# • "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.
#
# Input1:
# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course start
#
# Output1:
# 1.Arrays
# 2.Data Types
# 3.Objects
# 4.Databases
#
# Input2:
# Arrays, Lists, Methods
# Swap:Arrays:Methods
# Exercise:Databases
# Swap:Lists:Databases
# Insert:Arrays:0
# course start
#
# Output2:
# 1.Methods
# 2.Databases
# 3.Databases-Exercise
# 4.Arrays
# 5.Lists

def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons
def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)
    return list_of_lessons
def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):
            if 'Exercise' in list_of_lessons[title_index + 1]:
                list_of_lessons.pop(title_index + 1)
        list_of_lessons.remove(title)
    return list_of_lessons
def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_index = list_of_lessons.index(first_lesson)
        second_index = list_of_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_index + 1 in range(len(list_of_lessons)):
            first_has_exercise = 'Exercise' in list_of_lessons[first_index + 1]

        if second_index + 1 in range(len(list_of_lessons)):
            second_has_exercise = 'Exercise' in list_of_lessons[second_index + 1]
        list_of_lessons[first_index], list_of_lessons[second_index] = list_of_lessons[second_index], list_of_lessons[first_index]
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_index + 1], list_of_lessons[second_index + 1] = list_of_lessons[second_index + 1], list_of_lessons[first_index + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lessons.insert(first_index + 1, list_of_lessons.pop(second_index + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_index + 1, list_of_lessons.pop(first_index + 1))
    return list_of_lessons
def exercise(list_of_lessons, title):
    if title in list_of_lessons and f'{title}-Exercise' not in list_of_lessons:
        title_index = list_of_lessons.index(title)
        list_of_lessons.insert(title_index + 1, f'{title}-Exercise')
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(f'{title}-Exercise')
    return list_of_lessons

lessons = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')
    action = command[0]
    lesson_title = command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    if action == 'Add':
        lessons = add_lesson(lessons, lesson_title)
    elif action == 'Insert':
        lessons = insert_lesson(lessons, lesson_title, int(index_or_lesson_title))
    elif action == 'Remove':
        lessons = remove_lesson(lessons, lesson_title)
    elif action == 'Swap':
        lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
    elif action == 'Exercise':
        lessons = exercise(lessons, lesson_title)

    command = input()

for index, lesson_name in enumerate(lessons):
    print(f'{index + 1}.{lesson_name}')