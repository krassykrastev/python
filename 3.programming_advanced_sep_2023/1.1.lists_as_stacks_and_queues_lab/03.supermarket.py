# Tom is working at the supermarket, and he needs your help to keep track of his clients. Write a program that reads
# lines of input consisting of a customer's name and adds it to the end of a queue until "End" is received. If, in the
# meantime, you receive the command "Paid", you should print each customer in the order they are served (from
# the first to the last one) and empty the queue.
# When you receive "End", you should print the count of the remaining people in the queue in the format:
# "{count} people remaining."
#
# Input1:
# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End
#
# Output1:
# George
# Peter
# William
# 4 people remaining.
#
# Input2:
# Anna
# Emma
# Alexander
# End
#
# Output2:
# 3 people remaining.

from collections import deque

clients = deque()

while True:

    line_of_input = input()

    if line_of_input == "Paid":
        while clients:
            print(clients.popleft())

    elif line_of_input == "End":
        print(f"{len(clients)} people remaining.")
        break

    else:
        clients.append(line_of_input)
