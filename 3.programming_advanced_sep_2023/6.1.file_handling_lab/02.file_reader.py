# You are given a file called numbers.txt with the following content:
#     1
#     2
#     3
#     4
#     5
# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

import os
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, "numbers.txt")

file = open(file_path, "r")

total = 0

for line in file:
    current_num = int(line)
    total += current_num

print(total)
