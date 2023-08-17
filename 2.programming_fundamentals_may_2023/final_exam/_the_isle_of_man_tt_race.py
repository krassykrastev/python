import re

pattern = r"([#\$%\*&])([A-Za-z]+)\1=(\d+)!!(.+)"
line = input()
while line:
    result = re.findall(pattern, line)
    if result:
        name = result[0][1]
        length = int(result[0][2])
        encrypted_code = result[0][3]
        if length == len(encrypted_code):
            decrypted_code = [chr(ord(_) + length) for _ in encrypted_code]
            print(f"Coordinates found! {name} -> {''.join(decrypted_code)}")
    else:
        print("Nothing found!")
    line = input()