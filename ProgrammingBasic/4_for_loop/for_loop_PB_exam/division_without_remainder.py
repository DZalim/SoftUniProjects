count_n = int(input())

p1 = 0
p2 = 0
p3 = 0

for num in range (count_n):
    current_number = int(input())
    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1

percent_p1 = p1 / count_n * 100
percent_p2 = p2 / count_n * 100
percent_p3 = p3 / count_n * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
