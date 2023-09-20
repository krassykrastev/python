# Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you
# will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the
# intersection of these two ranges. The start and end numbers in the ranges are inclusive. Finally, you should find the
# longest intersection of all N intersections, print the numbers that are included and its length in the format:
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
#
# Input1:
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
#
# Output1:
# Longest intersection is [6, 7, 8, 9, 10] with length 5
#
# Input2:
# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11
#
# Output2:
# Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9

n = int(input())

longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    first_set = set(range(int(first_start), int(first_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))

    intersection = first_set.intersection(second_set)  # first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
