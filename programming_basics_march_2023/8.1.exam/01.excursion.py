number_of_people_in_group = int(input())
number_of_nights = int(input())
number_of_cards = int(input())
number_museum_tickets = int(input())

total_sum_to_pay = ((number_of_nights * 20) + (number_of_cards * 1.60) + (number_museum_tickets * 6)) * number_of_people_in_group
total_sum_to_pay *= 1.25

print(f'{total_sum_to_pay:.2f}')
