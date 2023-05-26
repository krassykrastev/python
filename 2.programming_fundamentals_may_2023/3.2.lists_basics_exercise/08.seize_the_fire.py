cells = input().split('#')
amount_of_water = int(input())
total_fire = 0
total_effort = 0
fire_out_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)

for cell in cells:
    type_of_fire, cell_value = cell.split(' = ')
    cell_value = int(cell_value)
    cell_is_valid = False
    if type_of_fire == 'High':
        if cell_value in high:
            cell_is_valid = True
    elif type_of_fire == 'Medium':
        if cell_value in medium:
            cell_is_valid = True
    elif type_of_fire == 'Low':
        if cell_value in low:
            cell_is_valid = True
    if cell_is_valid:
        if amount_of_water >= cell_value:
            amount_of_water -= cell_value
            fire_out_cells.append(cell_value)
            total_fire += cell_value
            total_effort += cell_value * 0.25

print('Cells:')
for fire_out_cell in fire_out_cells:
    print(f' - {fire_out_cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')