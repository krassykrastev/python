# You will be receiving to-do notes until you get the command "End".
# The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
#
# Input1:
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End
#
# Output1:
# ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
#
# Input2:
# 3-C
# 2-A
# 1-B
# 6-V
# End
#
# Output2:
# ['B', 'A', 'C', 'V']

def process_todo_notes():
    todo_notes = []

    while True:
        note = input()
        if note == 'End':
            break

        todo_notes.append(note)

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
    result_sorted_notes = [note.split('-')[1] for note in sorted_notes]
    return result_sorted_notes

result = process_todo_notes()
print(result)