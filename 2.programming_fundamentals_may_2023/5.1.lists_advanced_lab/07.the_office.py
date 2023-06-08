# You will receive two lines of input:
# • a list of employees' happiness as a string of numbers separated by a single space
# • a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# • If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# • Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"
#
# Input1:
# 1 2 3 4 2 1
# 3
#
# Output1:
# Score: 2/6. Employees are not happy!
#
# Input2:
# 2 3 2 1 3 3
# 4
#
# Output2:
# Score: 3/6. Employees are happy!

def check_employee_happiness():
    happiness_list = list(map(int, input().split(' ')))
    happiness_factor = int(input())

    improve_happiness = [h * happiness_factor for h in happiness_list]
    average_happiness = sum(improve_happiness) / len(improve_happiness)
    happy_count = sum(h >= average_happiness for h in improve_happiness)
    total_count = len(improve_happiness)
    message = 'happy' if happy_count >= total_count /2 else 'not happy'
    return f'Score: {happy_count}/{total_count}. Employees are {message}!'

result = check_employee_happiness()
print(result)