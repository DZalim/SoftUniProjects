number_of_moves = int(input())

points = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
invalid = 0

for move in range (number_of_moves):
    current_number = int(input())
    if 0 <= current_number <= 9:
        points += current_number * 0.20
        p1 +=1
    elif 10 <= current_number <= 19:
        points += current_number * 0.30
        p2 += 1
    elif 20 <= current_number <= 29:
        points += current_number * 0.40
        p3 += 1
    elif 30 <= current_number <= 39:
        points += 50
        p4 += 1
    elif 40 <= current_number <= 50:
        points += 100
        p5 += 1
    else:
        points *= 0.5
        invalid +=1

percent_p1 = p1 / number_of_moves * 100
percent_p2 = p2 / number_of_moves * 100
percent_p3 = p3 / number_of_moves * 100
percent_p4 = p4 / number_of_moves * 100
percent_p5 = p5 / number_of_moves * 100
percent_invalid = invalid / number_of_moves * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent_p1:.2f}%")
print(f"From 10 to 19: {percent_p2:.2f}%")
print(f"From 20 to 29: {percent_p3:.2f}%")
print(f"From 30 to 39: {percent_p4:.2f}%")
print(f"From 40 to 50: {percent_p5:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
