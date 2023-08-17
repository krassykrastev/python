import re

n = int(input())

pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<\1"

for _ in range(n):
    line = input()
    match = re.match(pattern, line)

    if match:
        decrypted = match.group(2) + match.group(3) + match.group(4) + match.group(5)
        print(f"Password: {decrypted}")
    else:
        print("Try another password!")