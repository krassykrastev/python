num_months = int(input())
expense_voda = 0
total_voda = 0
expense_net = 0
total_net = 0
expense_drugi = 0
total_drugi = 0
total_tok = 0

for i in range(num_months):
    expense_tok = float(input())
    total_tok += expense_tok
    expense_voda = 20
    total_voda += expense_voda
    expense_net = 15
    total_net += expense_net
    expense_drugi = (expense_tok + expense_voda + expense_net) + (expense_tok + expense_voda + expense_net) * 0.20
    total_drugi += expense_drugi
total_average = (total_tok + total_voda + total_net + total_drugi) / num_months

print(f'Electricity: {total_tok:.2f} lv')
print(f'Water: {total_voda:.2f} lv')
print(f'Internet: {total_net:.2f} lv')
print(f'Other: {total_drugi:.2f} lv')
print(f'Average: {total_average:.2f} lv')
