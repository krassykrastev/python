# You are a pianist, and you like to keep a list of your favorite piano pieces.
# Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format:
# "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
# •	"Add|{piece}|{composer}|{key}":
#   o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
#   o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
#   o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
#   o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
#   o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
#   o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# •	All the output messages with the appropriate formats are described in the problem description.
#
# Input1:
# 3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop
#
# Output1:
# Sonata No.2 by Chopin in B Minor added to the collection!
# Hungarian Rhapsody No.2 by Liszt in C# Minor added to the collection!
# Fur Elise is already in the collection!
# Successfully removed Clair de Lune!
# Changed the key of Moonlight Sonata to C# Major!
# Fur Elise -> Composer: Beethoven, Key: A Minor
# Moonlight Sonata -> Composer: Beethoven, Key: C# Major
# Sonata No.2 -> Composer: Chopin, Key: B Minor
# Hungarian Rhapsody No.2 -> Composer: Liszt, Key: C# Minor
#
# Input2:
# 4
# Eine kleine Nachtmusik|Mozart|G Major
# La Campanella|Liszt|G# Minor
# The Marriage of Figaro|Mozart|G Major
# Hungarian Dance No.5|Brahms|G Minor
# Add|Spring|Vivaldi|E Major
# Remove|The Marriage of Figaro
# Remove|Turkish March
# ChangeKey|Spring|C Major
# Add|Nocturne|Chopin|C# Minor
# Stop
#
# Output2:
# Spring by Vivaldi in E Major added to the collection!
# Successfully removed The Marriage of Figaro!
# Invalid operation! Turkish March does not exist in the collection.
# Changed the key of Spring to C Major!
# Nocturne by Chopin in C# Minor added to the collection!
# Eine kleine Nachtmusik -> Composer: Mozart, Key: G Major
# La Campanella -> Composer: Liszt, Key: G# Minor
# Hungarian Dance No.5 -> Composer: Brahms, Key: G Minor
# Spring -> Composer: Vivaldi, Key: C Major
# Nocturne -> Composer: Chopin, Key: C# Minor

n = int(input())
pieces = {}

for i in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {'composer': composer, 'key': key}

data = input()

while data != "Stop":
    command = data.split("|")
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()

for piece, data in pieces.items():
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")

# number_pieces = int(input())
#
# pieces_info = {}
#
# for piece in range(number_pieces):
#     piece_name, *info = input().split("|")
#     pieces_info[piece_name] = info
#
#
# def add_piece(piece, composer, key):
#     if piece in pieces_info:
#         return f"{piece} is already in the collection!"
#
#     pieces_info[piece] = [composer, key]
#     return f"{piece} by {composer} in {key} added to the collection!"
#
#
# def remove_piece(piece):
#     if piece in pieces_info:
#         del pieces_info[piece]
#         return f"Successfully removed {piece}!"
#     return f"Invalid operation! {piece} does not exist in the collection."
#
#
# def change_key(piece, new_key):
#     if piece in pieces_info:
#         pieces_info[piece][1] = new_key
#         return f"Changed the key of {piece} to {new_key}!"
#     return f"Invalid operation! {piece} does not exist in the collection."
#
#
# def show_result():
#     [print(f"{piece} -> Composer: {pieces_info[piece][0]}, Key: {pieces_info[piece][1]}") for piece in pieces_info]
#
#
# command_func = {
#     "Add": add_piece,
#     "Remove": remove_piece,
#     "ChangeKey": change_key
# }
#
# command = input()
# while command != "Stop":
#     command_type, *info = command.split("|")
#     print(command_func[command_type](*info))
#     command = input()
#
# show_result()
#
# number_of_pieces = int(input())
#
# music_info = {}
# piece_d, composer_d, key_d = "piece", "composer", "key"
#
#
# def piece_exists(piece_name: str):
#     if piece_name in music_info:
#         return True
#     return False
#
#
# def add_music_info(piece_name: str, composer_name: str, key_name: str, first_input: bool):
#     if piece_exists(piece_name):
#         if not first_input:
#             print(f"{piece_name} is already in the collection!")
#             return
#     if not piece_exists(piece_name):
#         music_info[piece_name] = music_info.get(piece_name, {})
#         music_info[piece_name][key_name] = composer_name
#         if not first_input:
#             print(f"{piece_name} by {composer_name} in {key_name} added to the collection!")
#
#
# def remove_music_info(piece_name: str):
#     if piece_exists(piece_name):
#         del music_info[piece_name]
#         return f"Successfully removed {piece_name}!"
#     return f"Invalid operation! {piece_name} does not exist in the collection."
#
#
# def change_music_info(piece_name: str, key_name: str):
#     if piece_exists(piece_name):
#         _, name_compositor = music_info[piece_name].popitem()
#         music_info[piece_name] = {}
#         music_info[piece_name][key_name] = name_compositor
#         return f"Changed the key of {piece_name} to {key_name}!"
#     return f"Invalid operation! {piece_name} does not exist in the collection."
#
#
# def show_result():
#     for piece_name in music_info:
#         for key, name in music_info[piece_name].items():
#             print(f"{piece_name} -> Composer: {name}, Key: {key}")
#
#
# for _ in range(number_of_pieces):
#     piece_name, composer_name, key_name = input().split("|")
#     add_music_info(piece_name, composer_name, key_name, True)
#
# command = input()
#
# while command != "Stop":
#     command_type, *info = command.split("|")
#     piece_name = info[0]
#     if command_type == "Remove":
#         print(remove_music_info(piece_name))
#     elif command_type == "Add":
#         composer_name = info[1]
#         key_name = info[2]
#         add_music_info(piece_name, composer_name, key_name, False)
#     elif command_type == "ChangeKey":
#         key_name = info[1]
#         print(change_music_info(piece_name, key_name))
#     command = input()
#
# show_result()
#
#
#
#





#
#
#
#
#
# number_of_pieces = int(input())
#
# music_info = {}
# result_info = list()
# piece_d = "piece"
# composer_d = "composer"
# key_d = "key"
#
#
# def add_music_info(piece_name, composer_name, key_name, first_input):
#     if piece_name in music_info:
#         if not first_input:
#             print(f"{piece_name} is already in the collection!")
#     elif piece_name not in music_info:
#         music_info[piece_name] = {}
#         music_info[piece_name][key_name] = composer_name
#         if not first_input:
#             print(f"{piece_name} by {composer_name} in {key_name} added to the collection!")
#
#
# def remove_music_info(piece_name):
#     if piece_name in music_info:
#         del music_info[piece_name]
#         print(f"Successfully removed {piece_name}!")
#     else:
#         print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#
# def change_music_info(piece_name, key_name):
#     if piece_name in music_info:
#         value = music_info[piece_name].popitem()
#         name_com = value[1]
#         # for key, value in music_info[piece_name].items():
#         #     name_com = value
#         # del music_info[piece_name]
#         music_info[piece_name] = {}
#         music_info[piece_name][key_name] = name_com
#         print(f"Changed the key of {piece_name} to {key_name}!")
#     else:
#         print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#
# def show_result():
#     for piece_name in music_info:
#         for key, name in music_info[piece_name].items():
#             result_info.append({piece_d: piece_name, composer_d: name, key_d: key})
#     result_info.sort(key=lambda item: (item[piece_d], item[composer_d]))
#     for info_display in result_info:
#         print(f"{info_display[piece_d]} -> Composer: {info_display[composer_d]}, Key: {info_display[key_d]}")
#
#
# for _ in range(number_of_pieces):
#     command = input().split("|")
#     piece_name = command[0]
#     composer_name = command[1]
#     key_name = command[2]
#     add_music_info(piece_name, composer_name, key_name, True)
#
# command = input()
#
# while command != "Stop":
#     command = command.split("|")
#     command_type = command[0]
#     piece_name = command[1]
#     if command_type == "Remove":
#         remove_music_info(piece_name)
#     elif command_type == "Add":
#         composer_name = command[2]
#         key_name = command[3]
#         add_music_info(piece_name, composer_name, key_name, False)
#     elif command_type == "ChangeKey":
#         key_name = command[2]
#         change_music_info(piece_name, key_name)
#     command = input()
#
# show_result()