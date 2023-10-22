def gather_credits(*kwargs):
    max_points = kwargs[0]
    credits = 0
    curses = []

    for curse_name, current_credits in kwargs[1:]:
        if curse_name not in curses:
            curses.append(curse_name)
            credits += current_credits
        if credits >= max_points:
            break

    if max_points > credits:
        return f"You need to enroll in more courses! You have to gather {max_points - credits} credits more."

    return f"Enrollment finished! Maximum credits: {credits}.\n" \
           f"Courses: {', '.join(sorted(curses))}"


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))