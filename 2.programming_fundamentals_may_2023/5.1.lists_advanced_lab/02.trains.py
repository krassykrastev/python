# You will receive a number representing the number of wagons a train has.
# Create a list (train) with the given length containing only zeros.
# Until you receive the command "End", you will receive some of the following commands:
# • "add {people}" – you should add the number of people in the last wagon
# • "insert {index} {people}" - you should add the number of people at the given wagon
# • "leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.
#
# Input1:
# 3
# add 20
# insert 0 15
# leave 0 5
# End
#
# Output1:
# [10, 0, 20]
#
# Input2:
# 5
# add 10
# add 20
# insert 0 16
# insert 1 44
# leave 1 12
# insert 2 100
# insert 4 61
# leave 4 1
# add 15
# End
#
# Output2:
# [16, 32, 100, 0, 105]

wagons = [0] * int(input())

while True:
    command = input().split(' ')

    if command[0] == 'End':
        print(wagons)
        break
    elif command[0] == 'add':
        number_of_people = int(command[1])
        wagons[-1] += number_of_people
    elif command[0] == 'insert':
        index = int(command[1])
        number_of_people = int(command[2])
        wagons[index] += number_of_people
    elif command[0] == 'leave':
        index = int(command[1])
        number_of_people = int(command[2])
        wagons[index] -= number_of_people