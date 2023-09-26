searched_book = input()

checked_books = 0

find_book = input()

while find_book != "No More Books":
    if find_book == searched_book:
        break
    checked_books += 1
    find_book = input()

if find_book != searched_book:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
else:
    print(f"You checked {checked_books} books and found it.")