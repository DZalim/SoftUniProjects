from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie('Predator', 1987, 10)

    def test_correct_initialization(self):
        self.assertEqual('Predator', self.movie.name)
        self.assertEqual(1987, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_raises_error(self):
        expected_message = "Name cannot be an empty string!"

        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual(expected_message, str(ve.exception))

    def test_year_setter_raises_error(self):
        expected_message = "Year is not valid!"

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1885

        self.assertEqual(expected_message, str(ve.exception))

    def test_add_actor_when_actor_does_not_existing(self):
        self.movie.add_actor('Arnold Schwarzenegger')
        self.assertEqual(['Arnold Schwarzenegger'], self.movie.actors)

    def test_add_actor_when_actor_existing(self):
        self.movie.actors = ['Arnold Schwarzenegger']
        result = self.movie.add_actor('Arnold Schwarzenegger')
        expected_message = "Arnold Schwarzenegger is already added in the list of actors!"

        self.assertEqual(expected_message, result)

    def test__gt__method_current_movie_greater(self):
        other_movie = Movie('Predator 2', 1988, 9)
        expected_message = '"Predator" is better than "Predator 2"'
        result = self.movie.__gt__(other_movie)
        self.assertEqual(expected_message, result)

    def test__gt__method_other_movie_greater(self):
        other_movie = Movie('Predator 2', 1988, 11)
        expected_message = '"Predator 2" is better than "Predator"'
        result = self.movie.__gt__(other_movie)
        self.assertEqual(expected_message, result)

    def test__repr_method(self):
        self.movie.actors = ['Arnold Schwarzenegger', 'Carl Weathers']

        expected_message = f"Name: Predator\n" \
               f"Year of Release: 1987\n" \
               f"Rating: 10.00\n" \
               f"Cast: Arnold Schwarzenegger, Carl Weathers"

        result = self.movie.__repr__()

        self.assertEqual(expected_message, result)


if __name__ == '__main__':
    main()
