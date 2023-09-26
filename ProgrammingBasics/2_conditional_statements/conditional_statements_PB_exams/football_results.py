first_match_result = input()
second_match_result = input()
third_match_result = input()

won = 0
lost = 0
drawn = 0

if first_match_result[0] > first_match_result[2]:
    won += 1
elif first_match_result[0] < first_match_result[2]:
    lost +=1
else:
    drawn +=1

if second_match_result[0] > second_match_result[2]:
    won += 1
elif second_match_result[0] < second_match_result[2]:
    lost += 1
else:
    drawn += 1

if third_match_result[0] > third_match_result[2]:
    won += 1
elif third_match_result[0] < third_match_result[2]:
    lost += 1
else:
    drawn += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")
