last_sector = input()
row_number_in_first_sector = int(input())
seat_number_in_odd_row = int(input())

first_sector = 'A'
number_of_rows = 0
seat_number_in_even_row = seat_number_in_odd_row + 2
combination = 0

for sectors in range(ord(first_sector), ord(last_sector) + 1):
    number_of_rows += 1
    for rows in range(1, row_number_in_first_sector + number_of_rows):
        if rows % 2 == 0:
            for seats in range(1, seat_number_in_even_row + 1):
                print(f'{chr(sectors)}{rows}{chr(96+seats)}')
                combination += 1
        else:
            for seats in range(1, seat_number_in_odd_row + 1):
                print(f'{chr(sectors)}{rows}{chr(96+seats)}')
                combination += 1
print(combination)
