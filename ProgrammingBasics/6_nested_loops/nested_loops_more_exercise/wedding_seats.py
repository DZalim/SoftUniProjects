last_sector = input()
number_of_rows_in_first_sector = int(input())
number_of_seats_in_odd_row = int(input())

total_seats = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, number_of_rows_in_first_sector + 1):
        if row % 2 != 0:
            for seats in range(1, number_of_seats_in_odd_row + 1):
                total_seats += 1
                print(f"{chr(sector)}{row}{chr(seats+96)}")
        else:
            for seats in range(1, number_of_seats_in_odd_row + 3):
                total_seats += 1
                print(f"{chr(sector)}{row}{chr(seats+96)}")
    number_of_rows_in_first_sector += 1
print(total_seats)