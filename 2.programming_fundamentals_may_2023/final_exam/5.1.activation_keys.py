# You are about to make some good money, but first, you need to think of a way to verify who paid for your product
# and who didn't. You have decided to let people use the software for a free trial period and then require an activation
# key to continue using the product. Before you can cash out, the last step is to design a program that creates unique
# activation keys for each user. So, waste no more time and start typing!
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different
# operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
# •	"Contains>>>{substring}":
#   o	If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
#   o	Otherwise, prints: "Substring not found!"
# •	"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
#   o	Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then
#   prints the activation key.
#   o	All given indexes will be valid.
# •	"Slice>>>{startIndex}>>>{endIndex}":
#   o	Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
#   o	Both indices will be valid.
#
# Input1:
# abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate
#
# Output1:
# abghijklmnopqrstuvwxyz
# abgHIJKLMNOPQRstuvwxyz
# abgHIjkLMNOPQRstuvwxyz
# Substring not found!
# Substring not found!
# Your activation key is: abgHIjkLMNOPQRstuvwxyz
#
# Input2:
# 134softsf5ftuni2020rockz42
# Slice>>>3>>>7
# Contains>>>-rock
# Contains>>>-uni-
# Contains>>>-rocks
# Flip>>>Upper>>>2>>>8
# Flip>>>Lower>>>5>>>11
# Generate
#
# Output2:
# 134sf5ftuni2020rockz42
# Substring not found!
# Substring not found!
# Substring not found!
# 134SF5FTuni2020rockz42
# 134SF5ftuni2020rockz42
# Your activation key is: 134SF5ftuni2020rockz42

key = input()

while True:
    command = input().split(">>>")

    if command[0] == "Generate":
        print(f"Your activation key is: {key}")
        break

    elif command[0] == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])

        if command[1] == "Upper":
            key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]

        elif command[1] == "Lower":
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]

        print(key)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        key = key[:start_index] + key[end_index:]
        print(key)
