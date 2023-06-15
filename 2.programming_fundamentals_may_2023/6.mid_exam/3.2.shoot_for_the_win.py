# Write a program that helps you keep track of your shot targets. You will receive a sequence with integers, separated by a single space,
# representing targets and their value. Afterward, you will be receiving indices until the "End" command is given,
# and you need to print the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered shot. Along with that, you also need to:
# •	Reduce all the other targets, which have greater values than your current target, with its value.
# •	Increase all the other targets, which have less than or equal value to the shot target, with its value.
# Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target, which is considered shot.
# When you receive the "End" command, print the targets in their current state and the count of shot targets in the following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"
# Input / Constraints
# •	On the first line of input, you will receive a sequence of integers, separated by a single space – the targets sequence.
# •	On the following lines, until the "End" command, you be receiving integers each on a single line – the index of the target to be shot.
#
# Input1:
# 24 50 36 70
# 0
# 4
# 3
# 1
# End
#
# Output1: Shot targets 3 -> -1 -1 130 -1
#
# Input2:
# 30 30 12 60 54 66
# 5
# 2
# 4
# 0
# End
#
# Output2: Shot targets: 4 -> -1 120 -1 66 -1 -1
sum_of_shot_targets = 0

list_of_targets = [int(target) for target in input().split(" ")]
index_of_shot_target = input()
targets_len = len(list_of_targets)

while index_of_shot_target != "End":
    index_of_shot_target = int(index_of_shot_target)

    if 0 <= index_of_shot_target < targets_len:
        target = list_of_targets[index_of_shot_target]
        list_of_targets[index_of_shot_target] = -1
        sum_of_shot_targets += 1

        for i in range(targets_len):
            if list_of_targets[i] == -1:
                continue
            if list_of_targets[i] > target:
                list_of_targets[i] -= target
            else:
                list_of_targets[i] += target

    index_of_shot_target = input()

print(f"Shot targets: {sum_of_shot_targets} ->", *list_of_targets)

# targets = [int(x) for x in input().split()]
# shoot = input()
# targets_len = len(targets)
#
# while shoot != "End":
#     shoot = int(shoot)
#
#     if 0 <= shoot < targets_len:
#         target = targets[shoot]
#         targets[shoot] = -1
#         for i in range(targets_len):
#
#             if targets[i] == -1:
#                 continue
#
#             if targets[i] > target:
#                 targets[i] -= target
#             else:
#                 targets[i] += target
#
#     shoot = input()
#
# print(f"Shot targets: {sum(1 for x in targets if x == -1)} ->", *targets)