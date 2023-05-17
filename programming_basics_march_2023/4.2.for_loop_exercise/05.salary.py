open_tabs = int(input())
salary = int(input())

for tab in range(open_tabs):
    curr_website = input()
    if curr_website == 'Facebook':
        salary -= 150
    elif curr_website == 'Instagram':
        salary -= 100
    elif curr_website == 'Reddit':
        salary -= 50
    
    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)
