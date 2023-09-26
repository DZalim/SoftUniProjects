hour = int(input())
minutes = int(input())

add_minutes = minutes + 15
total_hour = hour + (add_minutes // 60)
total_minutes = add_minutes % 60

if total_hour > 23:
    total_hour = 0

print(f"{total_hour}:{total_minutes:02d}")
