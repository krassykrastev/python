# Kate is stuck in a maze. You should help her to find her way out.
# On the first line, you will be given how many rows there are in the maze.
# On the following n lines, you will be given the maze itself.
# Here is a legend for the maze:
# • "#" - means a wall; Kate cannot go through there
# • " " - means empty space; Kate can go through there
# • "k" - the initial position of Kate; start looking for a way out from there
# There are two options: Kate either gets out or not:
# • If Kate can get out, print the following: "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
# • Otherwise, print: "Kate cannot get out".
#
# Input1:
# 4
# ######
# ##  k#
# ## ###
# ## ###
#
# Output1: Kate got out in 5 moves
#
# Input2:
# 5
# ######
# ##  k#
# ## ###
# ######
# ## ###
#
# Output2: Kate cannot get out
def find_position(maze):
    position = []
    for row in range(len(maze)):
        for el in maze[row]:
            if el == 'k':
                position.append(row)
                position.append(maze[row].find('k'))
                return position


def next_free_spot(maze):
    free_spots = []

    for row in range(len(maze)):
        for el in range(len(maze[row])):
            tmp = []
            if maze[row][el] == ' ':
                tmp.append(row)
                tmp.append(el)
                free_spots.insert(0, tmp)

    return free_spots


def find_path(position, next_free, maze):
    is_blocked = True
    step = 0
    moves = 0

    while step < len(next_free):
        x1 = next_free[step][0]
        x2 = next_free[step][1]
        temp = []
        temp.append(x1)
        temp.append(x2)
        # moving left
        if temp[0] == position[0] and position[1] - temp[1] == 1:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0
        # moving right
        elif temp[0] == position[0] and temp[1] - position[1] == 1:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0
        # moving down
        elif temp[0] - position[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0
        # moving up
        elif position[0] - temp[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            next_free.pop(step)
            step = 0


        else:

            step += 1

    if position[0] == 0 or position[0] == (len(maze) - 1) or position[1] == 0 or position[1] == len(maze[0]):
        return f'Kate got out in {moves + 1} moves'
    return f'Kate cannot get out'


m_rows = int(input())
maze = []
moves = 0
free_space = True
for row in range(m_rows):
    maze.append(input())
position = find_position(maze)
next_free = next_free_spot(maze)
movement = find_path(position, next_free, maze)
print(movement)