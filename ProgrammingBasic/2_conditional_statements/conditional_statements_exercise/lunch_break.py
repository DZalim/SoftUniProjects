import math

movie_name = input()
time_for_episodes = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break / 8
time_for_rest = time_for_break / 4
time_for_movie = time_for_break - time_for_lunch - time_for_rest

diff = math.ceil(abs(time_for_episodes - time_for_movie))

if time_for_movie >= time_for_episodes:
    print(f"You have enough time to watch {movie_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {diff} more minutes.")