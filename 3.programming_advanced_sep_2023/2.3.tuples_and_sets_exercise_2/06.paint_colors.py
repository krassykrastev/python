# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line containing substrings
# (separated by a single space) from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above
# colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
# •	orange = red + yellow
# •	purple = red + blue
# •	green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
# return them in the middle of the original string. If the string contains an odd number of substrings, you should put
# the substrings one position ahead. For example, if you are given the string "re yellow bye" you could not form a color
# with the substring "re" and "bye", so you should remove the last character and return them in the middle of the string:
# "r by yellow". In the end, print out the list with colors in the order in which they are found.
#
# Input1: d yel blu e low redd
# Output1: ['yellow', 'blue', 'red']
#
# Input2: r ue nge ora bl ed
# Output2: ['red', 'blue']
#
# Input3: re ple blu pop e pur d
# Output3: ['red', 'purple', 'blue']

from collections import deque

colors_string = deque(input().split())

main_colors = ["red", "blue", "yellow"]
secondary_colors = {"orange": ["red", "yellow"],
                    "purple": ["red", "blue"],
                    "green": ["blue", "yellow"]}

collected_colors = []

while colors_string:
    first_str = colors_string.popleft()
    last_str = colors_string.pop() if colors_string else ""
    if first_str + last_str in main_colors or first_str + last_str in secondary_colors:
        collected_colors.append(first_str + last_str)
    elif last_str + first_str in main_colors or last_str + first_str in secondary_colors:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            colors_string.insert(len(colors_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_string.insert(len(colors_string) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)
