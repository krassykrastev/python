# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin.
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space,
# representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence,
# you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line, you will receive a sequence of elements
# •	On the following lines, you will receive integers until the command "end"
# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - {element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message:
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following message:
# "Sorry you lose :(
# {the current sequence's state}"
#
# Input1:
# 1 1 2 2 3 3 4 4 5 5
# 1 0
# -1 0
# 1 0
# 1 0
# 1 0
# end
#
# Outpu1:
# Congrats! You have found matching elements - 1!
# Invalid input! Adding additional elements to the board
# Congrats! You have found matching elements - 2!
# Congrats! You have found matching elements - 3!
# Congrats! You have found matching elements - -2a!
# Sorry you lose :(
# 4 4 5 5
#
# Input2:
# a 2 4 a 2 4
# 0 3
# 0 2
# 0 1
# 0 1
# end
#
# Output2:
# Congrats! You have found matching elements - a!
# Congrats! You have found matching elements - 2!
# Congrats! You have found matching elements - 4!
# You have won in 3 turns!
#
# Input3:
# a 2 4 a 2 4
# 4 0
# 0 2
# 0 1
# 0 1
# end
#
# Output3:
# Try again!
# Try again!
# Try again!
# Try again!
# Sorry you lose :(
# a 2 4 a 2 4

list_of_elements = input().split()
command = input().split()
number_of_moves = 0
won = False

while command[0] != "end":
    number_of_moves += 1
    first_index = int(command[0])
    second_index = int(command[1])

    if first_index not in range(len(list_of_elements)) or second_index not in range(len(list_of_elements)) or first_index == second_index:
        list_of_elements.insert(int(len(list_of_elements) / 2), f"-{number_of_moves}a")
        list_of_elements.insert(int(len(list_of_elements) / 2), f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif list_of_elements[first_index] == list_of_elements[second_index]:
        found_element = list_of_elements[first_index]
        list_of_elements.remove(found_element), list_of_elements.remove(found_element)
        print(f"Congrats! You have found matching elements - {found_element}!")

    else:
        print(f"Try again!")

    if len(list_of_elements) == 0:
        won = True
        print(f'You have won in {number_of_moves} turns!')
        break

    command = input().split(" ")

if not won:
    print('Sorry you lose :(')
    print(*list_of_elements)

# elements = input().split()
# command = input().split()
# turns = 0
# won = False
#
# while command[0] != "end":
#     turns += 1
#     first_index = int(command[0])
#     second_index = int(command[1])
#
#     if first_index not in range(len(elements)) or second_index \
#             not in range(len(elements)) or first_index == second_index:
#         elements.insert(int(len(elements)/ 2), f"-{turns}a")
#         elements.insert(int(len(elements) / 2), f"-{turns}a")
#         print("Invalid input! Adding additional elements to the board")
#
#     elif elements[first_index] == elements[second_index]:
#         found_element = elements[first_index]
#         elements.remove(found_element), elements.remove(found_element)
#         print(f"Congrats! You have found matching elements - {found_element}!")
#
#     else:
#         print(f"Try again!")
#
#     if len(elements) == 0:
#         won = True
#         print(f'You have won in {turns} turns!')
#         break
#
#     command = input().split()
#
# if not won:
#     print(f'Sorry you lose :(\n{" ".join(elements)}')