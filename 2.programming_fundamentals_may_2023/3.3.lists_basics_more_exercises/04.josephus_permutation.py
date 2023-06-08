# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
# • the list itself - numbers separated by a single space representing the people in the circle
# • a number k People are standing in a circle waiting to be executed.
# Counting begins from the first one in the circle and proceeds from left to right.
# After a specified number of people are skipped, the k person is executed.
# The procedure is repeated with the remaining people, starting with the next person, going in the same direction,
# and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"
#
# Input1:
# 1 2 3 4 5 6 7
# 3
#
# Output1: [3,6,2,7,5,1,4]
#
# Input2: 10 5 65 104 1 0 2
# 8
#
# Output2: [10,65,0,1,5,2,104]

# solution by ceo as I was not able to find solution myself
main_list = input().split()
skip_number_k = int(input())

final_numbers = []
pos = skip_number_k - 1
index = 0
len_list = (len(main_list))

while len_list > 0:
    index = (pos + index) % len(main_list)
    final_numbers.append(main_list.pop(index))
    len_list -= 1

print(f"[{','.join(final_numbers)}]")