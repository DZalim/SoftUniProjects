number_of_men = int(input())
number_of_women = int(input())
number_of_tables = int(input())

counter = 0

for men in range(1, number_of_men + 1):
    for women in range(1, number_of_women + 1):
        counter += 1
        print(f"({men} <-> {women})", end= " ")
        if counter == number_of_tables:
            break
    if counter == number_of_tables:
        break
