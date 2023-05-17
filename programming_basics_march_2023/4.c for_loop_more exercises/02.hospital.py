number_of_days = int(input())
untreated_patients = 0
treated_patients = 0
doctors = 7

for i in range(1, number_of_days + 1):
    patients_current_day = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients_current_day > doctors:
        untreated_patients += patients_current_day - doctors
        treated_patients += doctors
    else:
        treated_patients += patients_current_day

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
