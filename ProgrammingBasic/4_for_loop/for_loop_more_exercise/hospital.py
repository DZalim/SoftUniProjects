period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period + 1):
    patient_per_day = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patient_per_day <= doctors:
        treated_patients += patient_per_day
    else:
        treated_patients_per_day = doctors
        treated_patients += treated_patients_per_day
        untreated_patients += patient_per_day - treated_patients_per_day

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

