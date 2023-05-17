movie_name = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_name != 'Finish':
    free_seats = int(input())
    tickets_for_movie = 0

    while free_seats > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        free_seats -= 1
        tickets_for_movie += 1

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

    percent_sold_tickets = tickets_for_movie / (free_seats + tickets_for_movie) * 100
    print(f'{movie_name} - {percent_sold_tickets:.2f}% full.')

    movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
