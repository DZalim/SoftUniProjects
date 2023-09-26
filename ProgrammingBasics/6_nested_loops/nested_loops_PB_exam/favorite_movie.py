movie_name = input()

max_points = 0
movie_with_max_points = ""
number_of_movies = 0
limit_is_reached = False

while movie_name != "STOP":
    number_of_movies += 1
    points = 0
    for letter in movie_name:
        points += ord(letter)
        if 65 <= ord(letter) <= 90:
            points -= len(movie_name)
        elif 97 <= ord(letter) <= 122:
            points -= len(movie_name) * 2
    if number_of_movies == 7:
        limit_is_reached = True
        break
    if points > max_points:
        max_points = points
        movie_with_max_points = movie_name
    movie_name = input()

if limit_is_reached:
    print("The limit is reached.")
print(f"The best movie for you is {movie_with_max_points} with {max_points} ASCII sum.")

