from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):

        if self.find_user(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        user = self.find_user(username)
        current_movie = self.find_movie(movie.title)

        if not user:
            raise Exception("This user does not exist!")

        if current_movie:
            raise "Movie already added to the collection!"

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.find_user(username)
        movie = self.find_movie(movie.title)

        if not movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.find_user(username)
        movie = self.find_movie(movie.title)

        if not movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.pop(user.movies_owned.index(movie))
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.find_user(username)
        movie = self.find_movie(movie.title)

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user(username)

        if not self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.pop(user.movies_liked.index(movie))

        return f"{username} disliked {movie.title} movie."

    # def display_movies(self):
    #
    #     sorted_movies = sorted([movie for movie in self.movies_collection],
    #                            key=lambda movie: (-movie.year, movie.title))
    #
    #     result = '\n'.join([movie.details() for movie in sorted_movies])
    #
    #     return result if result else "No movies found."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)

    # def __str__(self):
    #     users = ', '.join(user.username for user in self.users_collection)
    #     movies = ', '.join(movie.title for movie in self.movies_collection)
    #
    #     return (f"All users: {users if users else 'No users.'}\n"
    #             f"All movies: {movies if movies else 'No movies.'}")
    #
    def __str__(self):
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        return f'All users: {users}\nAll movies: {movies}'

    def find_user(self, username):
        user = [u for u in self.users_collection if u.username == username]
        return user[0] if user else None

    def find_movie(self, title):
        movie = [m for m in self.movies_collection if m.title == title]
        return movie[0] if movie else None

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False
