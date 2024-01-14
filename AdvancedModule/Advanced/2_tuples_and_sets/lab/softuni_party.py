reservation_numbers = set()

for _ in range(int(input())):
    reservation_numbers.add(input())

command = input()
while command != "END":
    if command in reservation_numbers:
        reservation_numbers.remove(command)
    command = input()

print(len(reservation_numbers))
for reservation in sorted(reservation_numbers):
    print(reservation)
