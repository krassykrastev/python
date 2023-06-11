# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
#
# Input1: 1
# Output1: 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes
#
# Input2: 5
# Output2: 5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes

centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
