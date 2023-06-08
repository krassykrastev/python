# You are at the zoo, and the meerkats look strange.
# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
# • On the first position is the head;
# • On the second position is the body;
# • On the last one is the tail.
#
# Input1:
# my tail
# my body seems on place
# my head is on the wrong end!
#
# Output1: ['my head is on the wrong end!', 'my body seems on place', 'my tail']
#
# Input2:
# tail
# body
# head
#
# Output2: ['head', 'body', 'tail']
#
# Input3:
# T
# B
# H
#
# Output3: ['H', 'B', 'T']

my_list = []
for i in range(3):
    data = input()
    my_list.append(data)
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)