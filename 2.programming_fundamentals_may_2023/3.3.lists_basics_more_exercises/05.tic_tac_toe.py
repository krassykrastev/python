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