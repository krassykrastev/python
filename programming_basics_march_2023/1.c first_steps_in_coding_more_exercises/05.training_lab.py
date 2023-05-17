w_in_meters = float(input())
h_in_meters = float(input())

w_in_cm = w_in_meters * 100
h_in_cm = h_in_meters * 100

number_of_desks_per_row = (h_in_cm - 100) // 70
number_of_rows = w_in_cm // 120
total_number_of_desks = (number_of_rows * number_of_desks_per_row) - 3

print(int(total_number_of_desks))
