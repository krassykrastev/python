money_as_string = input().split(', ')
number_of_beggars = int(input())
money_as_digits = []
final_sums = []
start_index = 0

for element in money_as_string:
    money_as_digits. append(int(element))

while start_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(start_index, len(money_as_digits), number_of_beggars):
        sum_for_current_beggar += money_as_digits[current_index]
    final_sums.append(sum_for_current_beggar)
    start_index += 1
print(final_sums)