# Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of depression.
# And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain Pokemon, those closest to you
# naturally get further, and those further from you, get closer.
# You will receive a sequence of integers, separated by spaces - the distances to the Pokemon.
# Then you will begin receiving integers, which will correspond to indexes in that sequence.
# When you receive an index, you must remove the element at that index from the sequence (as if you've captured the Pokemon).
# • You must increase the value of all elements in the sequence which are less or equal to the removed element with the value of the removed element.
# • You must decrease the value of all elements in the sequence which are greater than the removed element with the value of the removed element.
# If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
# If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy the first element to its place.
# The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.
# The program ends when the sequence has no elements (there are no Pokemon left for Ely to catch).
#
# Input1:
# 4 5 3
# 1
# 1
# 0
# Output1: 14
#
# Input2:
# 5 10 6 3 5
# 2
# 4
# 1
# 1
# 3
# 0
# 0
#
# Output2: 51

list_of_numbers = [int(s) for s in input().split(' ')]
list_of_removed_numbers = []

while list_of_numbers:
    index = int(input())

    if index < 0:
        number_to_be_removed = list_of_numbers.pop(0)
        list_of_numbers.insert(0, list_of_numbers[-1])

    elif index > len(list_of_numbers) - 1:
        number_to_be_removed = list_of_numbers.pop(-1)
        list_of_numbers.append(list_of_numbers[0])

    else:
        number_to_be_removed = list_of_numbers.pop(index)

    for number in range(len(list_of_numbers)):
        if list_of_numbers[number] <= number_to_be_removed:
            list_of_numbers[number] += number_to_be_removed
        else:
            list_of_numbers[number] -= number_to_be_removed

    list_of_removed_numbers.append(number_to_be_removed)

print(sum(list_of_removed_numbers))