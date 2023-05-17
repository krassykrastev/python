start_letter = input()
final_letter = input()
exclude_letter = input()
combinations = 0

for i in range(ord(start_letter), ord(final_letter) + 1):
    if chr(i) != exclude_letter:

        for j in range(ord(start_letter), ord(final_letter) + 1):
            if chr(j) != exclude_letter:

                for k in range(ord(start_letter), ord(final_letter) + 1):
                    if chr(k) != exclude_letter:
                        combinations += 1
                        print(f'{chr(i)}{chr(j)}{chr(k)}', end=' ')
print(combinations)
