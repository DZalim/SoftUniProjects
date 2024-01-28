def movie_organizer(*movie_info):
    movies = {}
    result = ''

    for movie_name, genre_group in movie_info:
        if genre_group not in movies:
            movies[genre_group] = []
        movies[genre_group].append(movie_name)

    sorted_movies = sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for genre, movies in sorted_movies:
        result += f'{genre} - {len(movies)}\n'
        for movie in sorted(movies):
            result += f'* {movie}\n'

    return result.strip()


print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
