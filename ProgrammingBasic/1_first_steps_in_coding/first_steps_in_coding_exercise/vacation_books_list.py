number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

needed_hours_per_whole_book = number_of_pages / pages_per_hour
hours_per_day = needed_hours_per_whole_book / number_of_days

print(int(hours_per_day))
