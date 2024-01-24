rows, cols = [int(el) for el in input().split()]

start_letter = ord('a')

for row in range(start_letter, start_letter + rows):
    for col in range(row, row + cols):
        print(f"{chr(row)}{chr(col)}{chr(row)}", end=' ')

    print()
