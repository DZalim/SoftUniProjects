import math

time_for_pictures = int(input())
number_of_scenes = int(input())
duration_of_scenes = int(input())

time_for_scenes = number_of_scenes * duration_of_scenes
field_preparation = time_for_pictures * 0.15
total_needed_time = time_for_scenes + field_preparation

diff = math.ceil(abs(time_for_pictures - total_needed_time))

if time_for_pictures >= total_needed_time:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")