name_of_the_serial = str(input())
number_of_seasons = int(input())
number_of_episodes = int(input())
duration_without_reklams = float(input())

reklams = 0.20 * duration_without_reklams
duration_of_the_episodes = duration_without_reklams + reklams
all_duration = int((number_of_episodes * number_of_seasons * duration_of_the_episodes) + (10 * number_of_seasons))

print(f"Total time needed to watch the {name_of_the_serial} series is {all_duration} minutes.")

