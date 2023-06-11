# Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves who pretend to be sheep.
# Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
# 4 3 2 1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep".
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
#
# Input1: sheep, sheep, wolf
# Output1: Please go away and stop eating my sheep
#
# Input2: wolf, sheep, sheep, sheep, sheep, sheep
# Output2: Oi! Sheep number 5! You are about to be eaten by a wolf!

sheep = 0

text = input()
my_list = list(text.split(', '))

for i in range(len(my_list) -1 , -1, -1):
    if my_list[-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    if my_list[i] == 'sheep':
        sheep += 1
    if my_list[i] == 'wolf':
        print(f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!')

# another solution from user:subtotal
# sheep_list = list(reversed(input().split(', ')))
#
# if sheep_list[0] == 'wolf':
#     print('Please go away and stop eating my sheep')
# else:
#     index = sheep_list.index('wolf')
#     print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')