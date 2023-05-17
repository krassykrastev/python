count_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_needed = count_pages // pages_per_hour # to receive integer number without float
hours_needed_per_day = hours_needed // days

print(hours_needed_per_day)
