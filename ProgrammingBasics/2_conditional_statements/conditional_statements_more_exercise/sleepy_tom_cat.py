number_of_days_off = int(input())

play_minutes_per_year = 30000
days_off_play_per_day = 127
work_days_play_per_day = 63
days_per_year = 365

play_work_days = (days_per_year - number_of_days_off) * work_days_play_per_day
play_day_off = number_of_days_off * days_off_play_per_day
total_play = play_day_off + play_work_days
diff = abs(play_minutes_per_year - total_play)
diff_hours = int(diff / 60)
diff_minutes = int(diff % 60)

if play_minutes_per_year < total_play:
    print("Tom will run away")
    print(f"{diff_hours} hours and {diff_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{diff_hours} hours and {diff_minutes} minutes less for play")


