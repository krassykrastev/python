# Create class Employee. Upon initialization, it should receive id (number), first_name (string), last_name (string),
# and salary (number). Create 3 additional instance methods:
# -	get_full_name() - returns "{first_name} {last_name}"
# -	get_annual_salary() - returns the total salary for 12 months
# -	raise_salary(amount) - increases the salary by the given amount and returns the new salary
#
# Test code:
# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())
#
# Output:
# John Smith
# 1500
# 18000

class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, salary: int):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount: int):
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
