total_liters = 0
total_alcohol_grad = 0

number_of_days = int(input())

for i in range(number_of_days):
    current_liters = float(input())
    current_alcohol_grad = float(input())

    total_liters += current_liters
    total_alcohol_grad += current_alcohol_grad * current_liters

average_alcohol_grad = total_alcohol_grad / total_liters
print(f'Liter: {total_liters:.2f}')
print(f'Degrees: {average_alcohol_grad:.2f}')

if average_alcohol_grad < 38:
    print(f'Not good, you should baking!')
elif average_alcohol_grad <= 42:
    print(f'Super!')
elif average_alcohol_grad > 42:
    print(f'Dilution with distilled water!')
