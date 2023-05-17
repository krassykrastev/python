num = input()
current_number = ''

for i in range(len(num)):
    current_number += str(int(num[i]))

biggest_number = sorted(current_number, reverse=True)

print(''.join(biggest_number))
