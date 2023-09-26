hour_exam = int(input())
minutes_exam = int(input())
hour_arriving = int(input())
minutes_arriving = int(input())

time_exam = hour_exam * 60 + minutes_exam
time_arriving = hour_arriving * 60 + minutes_arriving

if time_arriving > time_exam:
    print("Late")
elif time_arriving >= time_exam - 30:
    print("On time")
elif time_arriving < time_exam - 30:
    print("Early")

diff = abs(time_exam - time_arriving)
diff_hour = diff // 60
diff_minutes = diff % 60

if time_exam - 60 < time_arriving < time_exam:
    print(f"{diff_minutes} minutes before the start")
elif time_arriving <= time_exam - 60 <= time_exam:
    print(f"{diff_hour}:{diff_minutes:02d} hours before the start")
elif time_exam < time_arriving < time_exam + 60:
    print(f"{diff_minutes} minutes after the start")
elif time_exam <= time_exam + 60 <= time_arriving:
    print(f"{diff_hour}:{diff_minutes:02d} hours after the start")







