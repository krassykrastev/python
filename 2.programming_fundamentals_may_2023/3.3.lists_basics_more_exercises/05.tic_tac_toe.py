# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# • 0 - empty space
# • 1 - first player move
# • 2 - second player move
# Find out who the winner is. If the first player wins, print "First player won".
# If the second player wins, print "Second player won". Otherwise, print "Draw!".
#
# Input1:
# 2 0 1
# 0 1 0
# 1 0 2
#
# Output1: First player won
#
# Input2:
# 0 1 0
# 2 2 2
# 1 0 0
#
# Output2: Second player won
#
# Input3:
# 1 0 2
# 0 1 2
# 1 2 0
#
# Output3: Draw!

line_1 = input().split(' ')
line_2 = input().split(' ')
line_3 = input().split(' ')

if (line_1[0] == '1' and line_1[1] == '1' and line_1[2] == '1') or \
    (line_2[0] == '1' and line_2[1] == '1' and line_2[2] == '1') or \
    (line_3[0] == '1' and line_3[1] == '1' and line_3[2] == '1') or \
    (line_1[0] == '1' and line_2[0] == '1' and line_3[0] == '1') or \
    (line_1[1] == '1' and line_2[1] == '1' and line_3[1] == '1') or \
    (line_1[2] == '1' and line_2[2] == '1' and line_3[2] == '1') or \
    (line_1[0] == '1' and line_2[1] == '1' and line_3[2] == '1') or \
    (line_1[2] == '1' and line_2[1] == '1' and line_3[0] == '1'):
    print('First player won')
elif (line_1[0] == '2' and line_1[1] == '2' and line_1[2] == '2') or \
    (line_2[0] == '2' and line_2[1] == '2' and line_2[2] == '2') or \
    (line_3[0] == '2' and line_3[1] == '2' and line_3[2] == '2') or \
    (line_1[0] == '2' and line_2[0] == '2' and line_3[0] == '2') or \
    (line_1[1] == '2' and line_2[1] == '2' and line_3[1] == '2') or \
    (line_1[2] == '2' and line_2[2] == '2' and line_3[2] == '2') or \
    (line_1[0] == '2' and line_2[1] == '2' and line_3[2] == '2') or \
    (line_1[2] == '2' and line_2[1] == '2' and line_3[0] == '2'):
    print('Second player won')
else:
    print('Draw!')