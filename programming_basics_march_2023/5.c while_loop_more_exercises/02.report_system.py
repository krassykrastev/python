sum_from_sales = int(input())
payment = 1
card_payment = 0
cash_payment = 0
sales_from_cc = 0
sales_from_cash = 0
command = ''

while sum_from_sales > 0:
    command = input()
    if command == 'End':
        break

    current_price = int(command)

    if payment % 2 == 0:
        if current_price < 10:
            print('Error in transaction!')
        else:
            sales_from_cc += current_price
            sum_from_sales -= current_price
            card_payment += 1
            print('Product sold!')
    else:
        if current_price > 100:
            print('Error in transaction!')
        else:
            cash_payment += 1
            sales_from_cash += current_price
            sum_from_sales -= current_price
            print('Product sold!')

    payment += 1

if command == 'End':
    print('Failed to collect required money for charity.')
else:
    if cash_payment > 0:
        print(f'Average CS: {sales_from_cash / cash_payment:.2f}')
    if card_payment > 0:
        print(f'Average CC: {sales_from_cc / card_payment:.2f}')
