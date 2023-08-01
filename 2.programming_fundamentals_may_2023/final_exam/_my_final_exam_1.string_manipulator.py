initial_string = input()

while True:
    line = input()

    if line == "End":
        break

    data = line.split()

    if data[0] == "Translate":
        char = data[1]
        replacement = data[2]
        initial_string = initial_string.replace(char, replacement)
        print(initial_string)

    elif data[0] == "Includes":
        string = data[1]

        if string in initial_string:
            print("True")

        else:
            print("False")

    elif data[0] == "Start":
        string = data[1]
        print(initial_string.startswith(string))

    elif data[0] == "Lowercase":
        initial_string = initial_string.lower()
        print(initial_string)

    elif data[0] == "FindIndex":
        char = data[1]
        print(initial_string.rindex(char))

    elif data[0] == "Remove":
        start_i = int(data[1])
        count = int(data[2])
        to_remove = initial_string[start_i:start_i + count]
        initial_string = initial_string.replace(to_remove, "", 1)
        print(initial_string)
