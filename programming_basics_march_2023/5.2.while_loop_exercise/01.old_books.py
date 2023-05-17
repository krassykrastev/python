favorite_book = input()
current_book = input()

checked_books = 0
is_found = False

while current_book != 'No More Books':
    if current_book == favorite_book:
        is_found = True
        print(f'You checked {checked_books} books and found it.')
        break

    checked_books += 1
    current_book = input()

if not is_found:
    print('The book you search is not here!')
    print(f'You checked {checked_books} books.')
