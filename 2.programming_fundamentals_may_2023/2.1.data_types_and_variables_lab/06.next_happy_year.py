year = int(input())

while True:
    year += 1
    years_str = str(year)
    if len(set(years_str)) == len(years_str):
        break

print(year)
