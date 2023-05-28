# solution by ceo as I was not able to find solution myself
main_list = input().split()
skip_number_k = int(input())

final_numbers = []
pos = skip_number_k - 1
index = 0
len_list = (len(main_list))

while len_list > 0:
    index = (pos + index) % len(main_list)
    final_numbers.append(main_list.pop(index))
    len_list -= 1

print(f"[{','.join(final_numbers)}]")