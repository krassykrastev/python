budget = float(input())
number_of_gpu = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())
total_price = 0

price_gpu = number_of_gpu * 250
price_cpu = price_gpu * 0.35 * number_of_cpu
price_ram = price_gpu * 0.1 * number_of_ram


total_price = price_cpu + price_gpu + price_ram

if number_of_gpu > number_of_cpu:
    total_price *= 0.85 # получава 15% отстъпка от крайната цена, т.е. 0.85 от цялата променлива

diff = abs(total_price - budget)

if total_price <= budget:
    print(f'You have {diff:.2f} leva left!')

else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
