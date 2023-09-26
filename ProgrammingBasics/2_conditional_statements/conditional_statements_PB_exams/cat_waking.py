minutes_of_walk = int(input())
number_of_walks = int(input())
consumed_calories_for_day = int(input())

burned_calories = minutes_of_walk * 5 * number_of_walks
percent_burned_calories = (burned_calories / consumed_calories_for_day) * 100

if percent_burned_calories >= 50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")