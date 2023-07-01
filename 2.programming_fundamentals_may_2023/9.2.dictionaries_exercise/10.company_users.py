# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# • Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# • The input always will be valid.
#
# Input1:
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
#
# Output1:
# SoftUni
# -- AA12345
# -- BB12345
# Microsoft
# -- CC12345
# HP
# -- BB12345
#
# Input2:
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End
#
# Output2:
# SoftUni
# -- AA12345
# -- CC12344
# Lenovo
# -- XX23456
# Movement
# -- DD11111

companies = {}
command = input().split(" -> ")

while command[0] != "End":
    company = command[0]
    employee = command[1]
    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)
    command = input().split(" -> ")

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")