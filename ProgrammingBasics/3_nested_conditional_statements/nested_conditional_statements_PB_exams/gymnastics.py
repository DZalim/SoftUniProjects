country = input()
instrument = input()

grade_difficulty = 0
grade_performance = 0

if country == "Russia":
    if instrument == "ribbon":
        grade_difficulty = 9.1
        grade_performance = 9.4
    elif instrument == "hoop":
        grade_difficulty = 9.3
        grade_performance = 9.8
    elif instrument == "rope":
        grade_difficulty = 9.6
        grade_performance = 9
elif country == "Bulgaria":
    if instrument == "ribbon":
        grade_difficulty = 9.6
        grade_performance = 9.4
    elif instrument == "hoop":
        grade_difficulty = 9.55
        grade_performance = 9.75
    elif instrument == "rope":
        grade_difficulty = 9.5
        grade_performance = 9.4
elif country == "Italy":
    if instrument == "ribbon":
        grade_difficulty = 9.2
        grade_performance = 9.5
    elif instrument == "hoop":
        grade_difficulty = 9.45
        grade_performance = 9.35
    elif instrument == "rope":
        grade_difficulty = 9.7
        grade_performance = 9.15

total_grade = grade_performance + grade_difficulty
max_grade = 20
diff = abs(max_grade - total_grade)
percent = (diff / max_grade) * 100

print(f"The team of {country} get {total_grade:.3f} on {instrument}.")
print(f"{percent:.2f}%")


