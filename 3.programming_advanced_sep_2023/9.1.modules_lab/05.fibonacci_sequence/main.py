# Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence) and print them,
# separating them with a single space. The module should also be able to locate a specific number in the sequence.
# You can read more about the Fibonacci sequence here.
# You will be receiving commands until the "Stop" command. The commands are:
# •	"Create Sequence {count}". Create a series of numbers up to a specific count and print them in the following format:
#            "{n1} {n2} … {n}"
#
# •	"Locate {number}"
# Check if the sequence contains the number. If it finds the number, it should print:
# "The number - {number} is at index {index}"
# And if it doesn't find it:
# "The number {number} is not in the sequence"
#
# Input1:
# Create Sequence 10
# Locate 13
# Create Sequence 3
# Locate 10
# Stop
#
# Output1:
# 0 1 1 2 3 5 8 13 21 34
# The number - 13 is at index 7
# 0 1 1
# The number 10 is not in the sequence

from core.executor import play_fibonacci

play_fibonacci()
