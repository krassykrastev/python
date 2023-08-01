import re

pattern = r'^([%|\$])(?P<tag>[A-Z][a-z]{2,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

num_of_inputs = int(input())
decrypted_message = ''

for match in range(num_of_inputs):
    encrypted_message = input()

    if re.match(pattern, encrypted_message):
        matches = re.finditer(pattern, encrypted_message)
        for m in matches:
            decrypted_message = chr(int(m.group(3))) + chr(int(m.group(4))) + chr(int(m.group(5)))
            print(f"{m.group('tag')}: {decrypted_message}")
    else:
        print(f'Valid message not found!')
