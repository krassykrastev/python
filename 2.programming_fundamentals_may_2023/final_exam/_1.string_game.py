string = input()

command = input()

while command != "Done":
    data = command.split(" ")
    action = data[0]

    if action == "Change":
        char_one = data[1]
        replacement = data[2]

        string = string.replace(char_one, replacement)

        print(string)

    elif action == "Includes":
        substring_one = data[1]

        if substring_one in string:
            print("True")
        else:
            print("False")

    elif action == "End":
        substring = data[1]

        true_or_false = string.endswith(substring)

        print(true_or_false)

    elif action == "Uppercase":
        string = string.upper()

        print(string)

    elif action == "FindIndex":
        char = data[1]

        index = string.index(char)
        print(index)

    elif action == "Cut":
        first_index = int(data[1])
        count = int(data[2])

        string = string[first_index:first_index + count]

        print(string)

    command = input()

# def change(text, find, replace):
#     text = text.replace(find, replace)
#     return text
#
#
# def includes(text, substring):
#     if substring in text:
#         return True
#     return False
#
#
# def ends_with(text, substring):
#     if text.endswith(substring):
#         return True
#     return False
#
#
# def uppercase(text):
#     return text.upper()
#
#
# def find_char(text, char):
#     return text.index(char)
#
#
# def cut(text, start, end):
#     return text[start:end]
#
#
# def main():
#     text = input()
#     while True:
#         command = input().split()
#         if command[0] == "Done":
#             break
#         elif command[0] == "Change":
#             find = command[1]
#             replace = command[2]
#             text = change(text, find, replace)
#             print(text)
#         elif command[0] == "Includes":
#             substring = command[1]
#             print(includes(text, substring))
#         elif command[0] == "End":
#             substring = command[1]
#             print(ends_with(text, substring))
#         elif command[0] == "Uppercase":
#             text = uppercase(text)
#             print(text)
#         elif command[0] == "FindIndex":
#             char = command[1]
#             print(find_char(text, char))
#         elif command[0] == "Cut":
#             start_index = int(command[1])
#             end_index = start_index + int(command[2])
#             text = cut(text, start_index, end_index)
#             print(text)
#
#
# if __name__ == "__main__":
#     main()