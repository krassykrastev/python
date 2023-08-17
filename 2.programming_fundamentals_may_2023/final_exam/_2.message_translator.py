import re

number_of_strings = int(input())
pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

for _ in range(number_of_strings):
    text = input()
    matches = re.findall(pattern, text)
    if not matches:
        print("The message is invalid")
    else:
        for tuple_of_matches in matches:
            command = tuple_of_matches[0]
            string = tuple_of_matches[1]
            list_of_ascii = []
            for letter in string:
                list_of_ascii.append(ord(letter))
            string_of_numbers = [str(number) for number in list_of_ascii]
            print(f"{command}: {' '.join(string_of_numbers)}")