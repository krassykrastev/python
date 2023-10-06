# Create a program that will receive commands until the command "End". The commands can be:
# •	"Create-{file_name}" - Creates the given file with empty content. If the file already exists, remove the existing
# text in it (as if the file is created again)
# •	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it,
# and add the content
# •	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string
# with the new string. If the file does not exist, print: "An error occurred"
# •	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
#
# Input:
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End

import os

while True:
    line = input()
    if line == "End":
        break
    command, filename, *args = line.split("-")

    if command == "Create":
        open(filename, "w").close()

    elif command == "Add":
        with open(filename, "a") as file:
            file.write(f"{args[0]}\n")

    elif command == "Replace":
        try:
            with open(filename, "r") as file:
                content = file.read()

        except FileNotFoundError:
            print("An error occurred")

        else:
            with open(filename, "w") as file:
                content = content.replace(args[0], args[1])
                file.write(content)

    elif command == "Delete":
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("An error occurred")
