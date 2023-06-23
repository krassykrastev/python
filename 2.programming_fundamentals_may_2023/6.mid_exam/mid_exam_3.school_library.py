books = input().split('&')

while True:
    line = input()
    if line == 'Done':
        break

    tokens = line.split(' | ')
    command = tokens[0]
    if command == 'Add Book':
        name = tokens[1]
        if name not in books:
            books.insert(0, name)

    elif command == 'Take Book':
        name = tokens[1]
        if name in books:
            books.remove(name)

    elif command == 'Swap Books':
        first_book = tokens[1]
        second_book = tokens[2]
        first_i = None
        second_i = None
        if first_book in books and second_book in books:
            for i in range(len(books)):
                if books[i] == first_book:
                    first_i = i
                if books[i] == second_book:
                    second_i = i
                if first_i and second_i:
                    break
            books[first_i], books[second_i] = books[second_i], books[first_i]

    elif command == 'Insert Book':
        name = tokens[1]
        books.append(name)

    elif command == 'Check Book':
        index = int(tokens[1])
        if 0 <= index < len(books):
            print(books[index])

print(', '.join(books))