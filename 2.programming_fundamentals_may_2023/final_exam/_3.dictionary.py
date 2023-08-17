words_definitions = input().split(" | ")
dictionary = {}

for word_definition in words_definitions:
    data = word_definition.split(": ")
    key = data[0]
    value = data[1]

    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)

test_words = input().split(" | ")

command = input()
if command == "Test":
    for word in test_words:
        if word in dictionary.keys():
            print(word + ":")
            for definition in dictionary[word]:
                print(f" -{definition}")

elif command == "Hand Over":
    for key in dictionary.keys():
        print(key, end=" ")

# words = input().split(" | ")
# dictionary = {}
# for item in words:
#     word, definition = item.split(": ")
#     if word not in dictionary:
#         dictionary[word] = []
#     dictionary[word].append(definition)
# test_words = input().split(" | ")
# command = input()
# if command == "Test":
#     for test_word in test_words:
#         if test_word in dictionary:
#             print(f"{test_word}:")
#             for value in dictionary[test_word]:
#                 print(f" -{value}")
# elif command == "Hand Over":
#     print(*dictionary.keys())
#
#
# ################################################   Task Description   ################################################
# # 3. Dictionary