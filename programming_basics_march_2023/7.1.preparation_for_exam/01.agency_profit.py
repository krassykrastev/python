airline_name = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_tickets_price = float(input())
service_fee_price = float(input())

child_tickets_net_price = adult_tickets_price * 0.30
adult_ticket_price_with_fee = adult_tickets_price + service_fee_price
child_ticket_price_with_fee = child_tickets_net_price + service_fee_price
total_price_for_all_tickets = (adult_tickets * adult_ticket_price_with_fee) + (child_tickets * child_ticket_price_with_fee)
agency_profit = 0.2 * total_price_for_all_tickets

print(f'The profit of your agency from {airline_name} tickets is {agency_profit:.2f} lv.')
