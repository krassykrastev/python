def convert_grade_to_word(some_grade):
    if 2.00 <= some_grade <= 2.99:
        return 'Fail'
    elif 3.00 <= some_grade <= 3.49:
        return 'Poor'
    elif 3.50 <= some_grade <= 4.49:
        return 'Good'
    elif 4.50 <= some_grade <= 5.49:
        return 'Very Good'
    elif 5.50 <= some_grade <= 6.00:
        return 'Excellent'

grade = float(input())
result = convert_grade_to_word(grade)
print(result)