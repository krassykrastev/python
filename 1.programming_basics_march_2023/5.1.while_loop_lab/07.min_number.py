from sys import maxsize

min_number = maxsize

while True:
    command = input()
    if command == 'Stop':
        break
    current_number = int(command)
    if current_number < min_number:
        min_number = current_number

print(min_number)
