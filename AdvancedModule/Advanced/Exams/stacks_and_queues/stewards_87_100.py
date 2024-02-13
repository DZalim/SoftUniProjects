from collections import deque

seats = deque(input().split(', '))
first_sequence = deque([int(x) for x in input().split(', ')]) # queue
second_sequence = deque([int(x) for x in input().split(', ')]) # stack

rotation = 0
match_seats = []

while len(match_seats) != 3 and rotation != 10:
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    rotation += 1

    result = first_number + second_number
    ascii_char = chr(result)

    find_match_seat = False
    for seat in seats:
        if ascii_char in seat:
            find_match_seat = True
            if seat not in match_seats:
                match_seats.append(seat)
                break

    if not find_match_seat:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)
        seats.append(seats.popleft())

print(f"Seat matches: {', '.join(match_seats)}")
print(f'Rotations count: {rotation}')
