# Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value
# in the sequence, sorted in descending order.
# Input
# •	Read from the console a single line holding space-separated integers.
# Output
# •	Print the above-described numbers on a single line, space-separated.
# •	If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
# •	Print "No" if no numbers hold the above property.
#
# Input1: 10 20 30 40 50
# Output1: 50 40
#
# Input2: 5 2 3 4 -10 30 40 50 20 50 60 60 51
# Output2: 60 60 51 50 50
#
# Input3: 1
# Output3: No
#
# Input4: -1 -2 -3 -4 -5 -6
# Output4: -1 -2 -3

numbers = [int(x) for x in input().split(" ")]
average_number = sum(numbers) / len(numbers)
filtered_nums = sorted([x for x in numbers if x > average_number])

if filtered_nums:
    for i in range(5):
        if filtered_nums:
            print(filtered_nums.pop(), end=" ")
else:
    print("No")