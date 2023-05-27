message = []
list_of_numbers_as_string = input().split(' ')
text = input()

for i in range(len(list_of_numbers_as_string)):
    sum = 0
    for digit in list_of_numbers_as_string[i]:
        sum += int(digit)
        while sum >= len(text):
            sum -= len(text)
    message.append(text[sum])
    text = text[:sum] + text[sum + 1:]

print(*message, sep='')